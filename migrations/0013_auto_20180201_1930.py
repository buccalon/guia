# Generated by Django 2.0.1 on 2018-02-01 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guia', '0012_auto_20180201_1908'),
    ]

    operations = [
        migrations.AlterField(
            model_name='colecao',
            name='entry_obs',
            field=models.TextField(blank=True, help_text='Insira observações sobre a coleção', max_length=1000, null=True, verbose_name='Observações'),
        ),
    ]
