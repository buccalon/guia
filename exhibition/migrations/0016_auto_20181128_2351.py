# Generated by Django 2.0.5 on 2018-11-29 01:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exhibition', '0015_remove_exhibition_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exhibition',
            name='docs',
            field=models.ManyToManyField(blank=True, related_name='exhibitionDoc', to='digitalassetsmanagement.Doc', verbose_name='Documents'),
        ),
    ]
