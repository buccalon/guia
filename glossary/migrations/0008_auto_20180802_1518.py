# Generated by Django 2.0.5 on 2018-08-02 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('glossary', '0007_auto_20180727_1626'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accesscondition',
            name='title',
            field=models.CharField(blank=True, default=None, help_text='Ex.: The title of this record', max_length=256, null=True, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='aggregationtype',
            name='title',
            field=models.CharField(blank=True, default=None, help_text='Ex.: The title of this record', max_length=256, null=True, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='descriptionlevel',
            name='title',
            field=models.CharField(blank=True, default=None, help_text='Ex.: The title of this record', max_length=256, null=True, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='genretag',
            name='title',
            field=models.CharField(blank=True, default=None, help_text='Ex.: The title of this record', max_length=256, null=True, verbose_name='Title'),
        ),
    ]
