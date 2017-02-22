from .models import Field


def reload_fields_schema(model):
    field = model._meta.get_field('data')
    field.reload_schema(
        [each_field.field_type for each_field in Field.objects.all() if each_field.field_type]
    )
