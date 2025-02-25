# Generated by Django 2.0.5 on 2018-11-28 23:13

from django.db import migrations


def fill_locations(apps, schema_editor):
    exhibition_model = apps.get_model('exhibition', 'Exhibition')

    for exhibition in exhibition_model.objects.filter(location__isnull=False):
        exhibition.locations.add(exhibition.location)


def back_fill_locations(apps, schema_editor):
    exhibition_model = apps.get_model('exhibition', 'Exhibition')
    for exhibition in exhibition_model.objects.filter(location__isnull=False):
        exhibition.locations.clear()


class Migration(migrations.Migration):

    dependencies = [
        ('exhibition', '0013_auto_20181128_2112'),
    ]

    operations = [
        migrations.RunPython(fill_locations, back_fill_locations)
    ]
