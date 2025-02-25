# Generated by Django 2.0.5 on 2018-11-20 23:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0008_auto_20181022_1542'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='is_draft',
            field=models.BooleanField(db_index=True, default=False, help_text='Objects as "draft" are not available on the website', verbose_name='Is draft?'),
        ),
    ]
