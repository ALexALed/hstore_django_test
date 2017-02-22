from __future__ import unicode_literals

from django.db import models
from django_hstore import hstore

from django.contrib.postgres.fields import JSONField


class Field(models.Model):
    name = models.CharField(max_length=100)
    field_type = JSONField(default={
            'name': 'field',
            'class': 'IntegerField',
            'kwargs': {
                'default': 0
            }
        }
    )


class TestModel(models.Model):
    name = models.CharField(max_length=100)
    data = hstore.DictionaryField()
