# Generated by Django 2.0.5 on 2018-07-11 17:19

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('publication', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PublicationType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Auto set field', verbose_name='Created in')),
                ('title', models.CharField(help_text='Ex.: book', max_length=256, verbose_name='Title')),
                ('description', models.CharField(blank=True, help_text='Ex.: A book is...', max_length=512, null=True, verbose_name='Description')),
            ],
            options={
                'verbose_name': 'Publication Type',
                'verbose_name_plural': 'Publication Types',
            },
        ),
        migrations.AddField(
            model_name='publication',
            name='dimension',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, help_text='Feed with information about dimensions', null=True, verbose_name='Dimensions'),
        ),
        migrations.AddField(
            model_name='publication',
            name='other_data',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, help_text='Other unstructured data of this publication', null=True, verbose_name='Other Data'),
        ),
        migrations.AddField(
            model_name='publication',
            name='pages',
            field=models.PositiveIntegerField(blank=True, help_text='Total number of pages', null=True, verbose_name='Number of pages'),
        ),
        migrations.AlterField(
            model_name='publication',
            name='title',
            field=models.CharField(default='No title publication', help_text='Ex.: The complete photo collection of Sebastião Salgado.', max_length=256, verbose_name='Title'),
        ),
        migrations.AddField(
            model_name='publication',
            name='type',
            field=models.ForeignKey(blank=True, help_text='Choose the more appropriate type to means this publication', null=True, on_delete=django.db.models.deletion.SET_NULL, to='publication.PublicationType', verbose_name='Type'),
        ),
    ]
