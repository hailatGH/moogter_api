# Generated by Django 2.2 on 2020-09-08 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0004_minisuggestionmessage'),
    ]

    operations = [
        migrations.AddField(
            model_name='conversation',
            name='last_message',
            field=models.CharField(max_length=560, null=True),
        ),
    ]
