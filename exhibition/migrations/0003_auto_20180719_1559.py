# Generated by Django 2.0.5 on 2018-07-19 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exhibition', '0002_exhibitionedition_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exhibition',
            name='slug',
            field=models.SlugField(blank=True, help_text='Ex.: complete-collection-sebastiao-salgado', max_length=256, null=True, unique=True, verbose_name='Slug'),
        ),
    ]
