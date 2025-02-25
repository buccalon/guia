# Generated by Django 2.0.5 on 2018-07-23 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('digitalassetsmanagement', '0004_auto_20180723_1600'),
        ('person', '0003_auto_20180723_1403'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='thumbnail',
        ),
        migrations.AddField(
            model_name='person',
            name='capture',
            field=models.ManyToManyField(blank=True, help_text='Choose some introduction and representative images', to='digitalassetsmanagement.Capture', verbose_name='Captures'),
        ),
    ]
