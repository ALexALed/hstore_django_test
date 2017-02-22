from django.test import TestCase

from .models import Field, TestModel
from utils import reload_fields_schema


class TestHStore(TestCase):
    def test_first(self):
        field = Field(name='first', field_type={
            'name': 'choice',
            'class': 'CharField',
            'kwargs': {
                'blank': True,
                'max_length': 10,
                'choices': (('choice1', 'choice1'), ('choice2', 'choice2'))
            }
        })
        field.save()
        self.assertEqual(Field.objects.count(), 1)
        reload_fields_schema(TestModel)
        tmo = TestModel(name='first', data={'choice': 'choice1', 'hello': 1122})
        tmo.save()
        self.assertEqual(TestModel.objects.count(), 1)
