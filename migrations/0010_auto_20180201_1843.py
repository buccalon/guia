# Generated by Django 2.0.1 on 2018-02-01 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guia', '0009_auto_20180201_1842'),
    ]

    operations = [
        migrations.AlterField(
            model_name='colecao',
            name='id',
            field=models.CharField(help_text='Código de identificação', max_length=20, primary_key=True, serialize=False, unique=True),
        ),
    ]
