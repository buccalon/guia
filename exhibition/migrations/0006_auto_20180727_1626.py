# Generated by Django 2.0.5 on 2018-07-27 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exhibition', '0005_auto_20180724_1756'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exhibition',
            name='slug',
            field=models.SlugField(blank=True, default=None, help_text='Ex.: complete-collection-sebastiao-salgado', max_length=256, null=True, unique=True, verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='exhibition',
            name='title',
            field=models.CharField(default=None, help_text='Ex.: The title of this record', max_length=256, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='exhibitionedition',
            name='slug',
            field=models.SlugField(blank=True, default=None, help_text='Ex.: complete-collection-sebastiao-salgado', max_length=256, null=True, unique=True, verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='exhibitionedition',
            name='title',
            field=models.CharField(default=None, help_text='Ex.: The title of this record', max_length=256, verbose_name='Title'),
        ),
    ]
