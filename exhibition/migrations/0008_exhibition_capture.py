# Generated by Django 2.0.5 on 2018-09-22 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('digitalassetsmanagement', '0008_auto_20180802_1518'),
        ('exhibition', '0007_auto_20180802_1518'),
    ]

    operations = [
        migrations.AddField(
            model_name='exhibition',
            name='capture',
            field=models.ManyToManyField(blank=True, help_text='Choose some introduction and representative images', to='digitalassetsmanagement.Capture', verbose_name='Capture'),
        ),
    ]
