# Generated by Django 2.0.5 on 2018-07-23 17:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0004_auto_20180719_1855'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='collection',
            name='items',
        ),
    ]
