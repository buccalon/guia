# Generated by Django 2.0.5 on 2018-07-23 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('digitalassetsmanagement', '0003_auto_20180719_1855'),
        ('collection', '0005_remove_collection_items'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='collection',
            name='thumbnail',
        ),
        migrations.AddField(
            model_name='collection',
            name='capture',
            field=models.ManyToManyField(blank=True, help_text='Choose some introduction and representative images', to='digitalassetsmanagement.Capture', verbose_name='Capture'),
        ),
    ]
