# Generated by Django 2.0.1 on 2018-02-01 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guia', '0015_auto_20180201_1944'),
    ]

    operations = [
        migrations.AlterField(
            model_name='colecao',
            name='id',
            field=models.CharField(help_text='Código de identificação', max_length=20, primary_key=True, serialize=False, verbose_name='Código (UID)'),
        ),
    ]
