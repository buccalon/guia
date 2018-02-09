# Generated by Django 2.0.1 on 2018-02-01 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guia', '0011_auto_20180201_1906'),
    ]

    operations = [
        migrations.AlterField(
            model_name='colecao',
            name='entry_obs',
            field=models.TextField(blank=True, help_text='Insira observações sobre a coleção', max_length=300, null=True, verbose_name='Observações'),
        ),
        migrations.AlterField(
            model_name='colecao',
            name='id',
            field=models.CharField(help_text='Código de identificação', max_length=20, primary_key=True, serialize=False, unique=True, verbose_name='Código (UID)'),
        ),
    ]
