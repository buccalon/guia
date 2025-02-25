# Generated by Django 2.0.5 on 2018-11-20 23:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0007_auto_20180802_1518'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='is_draft',
            field=models.BooleanField(db_index=True, default=False, help_text='Objects as "draft" are not available on the website', verbose_name='Is draft?'),
        ),
    ]
