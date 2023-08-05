from django.db.models import CharField, Max
from django.db.models.functions import Lower
from django.test import TestCase, skipUnlessDBFeature
from django.test.utils import register_lookup

from .models import Celebrity, Fan, Staff, StaffTag, Tag


@skipUnlessDBFeature('can_distinct_on_fields')
@skipUnlessDBFeature('supports_nullable_unique_constraints')
class DistinctOnTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.t1 = Tag.objects.create(name='t1')
        cls.t2 = Tag.objects.create(name='t2', parent=cls.t1)
        cls.t3 = Tag.objects.create(name='t3', parent=cls.t1)
        cls.t4 = Tag.objects.create(name='t4', parent=cls.t3)
        cls.t5 = Tag.objects.create(name='t5', parent=cls.t3)

        cls.p1_o1 = Staff.objects.create(id=1, name="p1", organisation="o1")
        cls.p2_o1 = Staff.objects.create(id=2, name="p2", organisation="o1")
        cls.p3_o1 = Staff.objects.create(id=3, name="p3", organisation="o1")
        cls.p1_o2 = Staff.objects.create(id=4, name="p1", organisation="o2")
        cls.p1_o1.coworkers.add(cls.p2_o1, cls.p3_o1)
        StaffTag.objects.create(staff=cls.p1_o1, tag=cls.t1)
        StaffTag.objects.create(staff=cls.p1_o1, tag=cls.t1)

        celeb1 = Celebrity.objects.create(name="c1")
        celeb2 = Celebrity.objects.create(name="c2")

        cls.fan1 = Fan.objects.create(fan_of=celeb1)
        cls.fan2 = Fan.objects.create(fan_of=celeb1)
        cls.fan3 = Fan.objects.create(fan_of=celeb2)

    def test_basic_distinct_on(self):
        """QuerySet.distinct('field', ...) works"""
        # (qset, expected) tuples
        qsets = (
            (
                Staff.objects.distinct().order_by('name'),
                ['<Staff: p1>', '<Staff: p1>', '<Staff: p2>', '<Staff: p3>'],
            ),
            (
                Staff.objects.distinct('name').order_by('name'),
                ['<Staff: p1>', '<Staff: p2>', '<Staff: p3>'],
            ),
            (
                Staff.objects.distinct('organisation').order_by('organisation', 'name'),
                ['<Staff: p1>', '<Staff: p1>'],
            ),
            (
                Staff.objects.distinct('name', 'organisation').order_by('name', 'organisation'),
                ['<Staff: p1>', '<Staff: p1>', '<Staff: p2>', '<Staff: p3>'],
            ),
            (
                Celebrity.objects.filter(fan__in=[self.fan1, self.fan2, self.fan3]).distinct('name').order_by('name'),
                ['<Celebrity: c1>', '<Celebrity: c2>'],
            ),
            # Does combining querysets work?
            (
                (Celebrity.objects.filter(fan__in=[self.fan1, self.fan2]).
                    distinct('name').order_by('name') |
                 Celebrity.objects.filter(fan__in=[self.fan3]).
                    distinct('name').order_by('name')),
                ['<Celebrity: c1>', '<Celebrity: c2>'],
            ),
            (
                StaffTag.objects.distinct('staff', 'tag'),
                ['<StaffTag: t1 -> p1>'],
            ),
            (
                Tag.objects.order_by('parent__pk', 'pk').distinct('parent'),
                ['<Tag: t2>', '<Tag: t4>', '<Tag: t1>'],
            ),
            (
                StaffTag.objects.select_related('staff').distinct('staff__name').order_by('staff__name'),
                ['<StaffTag: t1 -> p1>'],
            ),
            # Fetch the alphabetically first coworker for each worker
            (
                (Staff.objects.distinct('id').order_by('id', 'coworkers__name').
                    values_list('id', 'coworkers__name')),
                ["(1, 'p2')", "(2, 'p1')", "(3, 'p1')", "(4, None)"]
            ),
        )
        for qset, expected in qsets:
            self.assertQuerysetEqual(qset, expected)
            self.assertEqual(qset.count(), len(expected))

        # Combining queries with different distinct_fields is not allowed.
        base_qs = Celebrity.objects.all()
        with self.assertRaisesMessage(AssertionError, "Cannot combine queries with different distinct fields."):
            base_qs.distinct('id') & base_qs.distinct('name')

        # Test join unreffing
        c1 = Celebrity.objects.distinct('greatest_fan__id', 'greatest_fan__fan_of')
        self.assertIn('OUTER JOIN', str(c1.query))
        c2 = c1.distinct('pk')
        self.assertNotIn('OUTER JOIN', str(c2.query))

    def test_transform(self):
        new_name = self.t1.name.upper()
        self.assertNotEqual(self.t1.name, new_name)
        Tag.objects.create(name=new_name)
        with register_lookup(CharField, Lower):
            self.assertCountEqual(
                Tag.objects.order_by().distinct('name__lower'),
                [self.t1, self.t2, self.t3, self.t4, self.t5],
            )

    def test_distinct_not_implemented_checks(self):
        # distinct + annotate not allowed
        msg = 'annotate() + distinct(fields) is not implemented.'
        with self.assertRaisesMessage(NotImplementedError, msg):
            Celebrity.objects.annotate(Max('id')).distinct('id')[0]
        with self.assertRaisesMessage(NotImplementedError, msg):
            Celebrity.objects.distinct('id').annotate(Max('id'))[0]

        # However this check is done only when the query executes, so you
        # can use distinct() to remove the fields before execution.
        Celebrity.objects.distinct('id').annotate(Max('id')).distinct()[0]
        # distinct + aggregate not allowed
        msg = 'aggregate() + distinct(fields) not implemented.'
        with self.assertRaisesMessage(NotImplementedError, msg):
            Celebrity.objects.distinct('id').aggregate(Max('id'))

    def test_distinct_on_in_ordered_subquery(self):
        qs = Staff.objects.distinct('name').order_by('name', 'id')
        qs = Staff.objects.filter(pk__in=qs).order_by('name')
        self.assertSequenceEqual(qs, [self.p1_o1, self.p2_o1, self.p3_o1])
        qs = Staff.objects.distinct('name').order_by('name', '-id')
        qs = Staff.objects.filter(pk__in=qs).order_by('name')
        self.assertSequenceEqual(qs, [self.p1_o2, self.p2_o1, self.p3_o1])

    def test_distinct_on_get_ordering_preserved(self):
        """
        Ordering shouldn't be cleared when distinct on fields are specified.
        refs #25081
        """
        staff = Staff.objects.distinct('name').order_by('name', '-organisation').get(name='p1')
        self.assertEqual(staff.organisation, 'o2')
