# Generated by Django 2.0.5 on 2018-07-27 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0005_person_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='slug',
            field=models.SlugField(blank=True, default=None, help_text='Ex.: complete-collection-sebastiao-salgado', max_length=256, null=True, unique=True, verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='person',
            name='title',
            field=models.CharField(default=None, help_text='Ex.: The title of this record', max_length=256, verbose_name='Title'),
        ),
    ]
