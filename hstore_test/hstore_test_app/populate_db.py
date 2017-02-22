from .models import Field, TestModel
from utils import reload_fields_schema


def populate_db():
    Field.objects.all().delete()
    TestModel.objects.all().delete()

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
    print(Field.objects.count())
    reload_fields_schema(TestModel)
    tmo = TestModel(name='first', data={'choice': 'choice1', 'hello': '1122'})  # field hello does not exists in schema but saved done
    tmo.save()
    print(TestModel.objects.count())

    field = Field(name='second', field_type={
        'name': 'num',
        'class': 'IntegerField',
    })
    field.save()
    print(Field.objects.count())
    reload_fields_schema(TestModel)

    tmo = TestModel(name='second')
    # tmo.num = 'dsfsdf324234'
    # print(tmo.num) - if uncomment we get validation error
    tmo.num = 1000
    tmo.save()
    print(TestModel.objects.count())
    refresh_tmo = TestModel.objects.filter(name='second').last()
    print(refresh_tmo.num)  # Virtual field value
    print(type(refresh_tmo.num))  # Virtual field type
