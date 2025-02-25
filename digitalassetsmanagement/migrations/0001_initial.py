# Generated by Django 2.0.5 on 2018-07-14 21:35

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Capture',
            fields=[
                ('id_auto_series', models.BigAutoField(editable=False, help_text='Auto Increment ID', primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, help_text='This is an auto set field', unique=True, verbose_name='Universal Unique Identifier')),
                ('title', models.CharField(blank=True, help_text='Ex.: The capture title', max_length=256, null=True, verbose_name='Title')),
            ],
            options={
                'verbose_name': 'Capture',
                'verbose_name_plural': 'Captures',
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id_auto_series', models.BigAutoField(editable=False, help_text='Auto Increment ID', primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, help_text='This is an auto set field', unique=True, verbose_name='Universal Unique Identifier')),
                ('id_human', models.CharField(blank=True, help_text='Institucional Identifier', max_length=64, null=True, unique=True, verbose_name='Institucional ID')),
                ('title', models.CharField(help_text='Ex.: Salgado Negative - 001', max_length=256, verbose_name='Title')),
                ('description', models.TextField(blank=True, help_text='Ex.: Gelatin negative of the first photo...', null=True, verbose_name='Description')),
                ('capture', models.ManyToManyField(blank=True, help_text='Capture(s) taked from this item.', to='digitalassetsmanagement.Capture', verbose_name='Capture(s)')),
            ],
            options={
                'verbose_name': 'Item',
                'verbose_name_plural': 'Items',
            },
        ),
        migrations.CreateModel(
            name='Thumbnail',
            fields=[
                ('id_auto_series', models.BigAutoField(editable=False, help_text='Auto Increment ID', primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, help_text='This is an auto set field', unique=True, verbose_name='Universal Unique Identifier')),
                ('title', models.CharField(blank=True, help_text='Ex.: Image title, like "the photographer resting" ', max_length=256, null=True, verbose_name='Title')),
                ('image', models.ImageField(help_text='The Image File', upload_to='', verbose_name='Image')),
            ],
            options={
                'verbose_name': 'Thumbnail',
                'verbose_name_plural': 'Thumbnails',
            },
        ),
        migrations.AddField(
            model_name='capture',
            name='thumbnail',
            field=models.ForeignKey(blank=True, help_text='Choose the image whish represents this capture', null=True, on_delete=django.db.models.deletion.SET_NULL, to='digitalassetsmanagement.Thumbnail', verbose_name='Thumbnails'),
        ),
    ]
