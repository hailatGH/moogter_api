# Generated by Django 2.2 on 2020-07-28 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('views', '0003_view_is_edited'),
    ]

    operations = [
        migrations.AddField(
            model_name='view',
            name='is_removed',
            field=models.BooleanField(default=False),
        ),
    ]
