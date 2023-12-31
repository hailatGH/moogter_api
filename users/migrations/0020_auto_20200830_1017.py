# Generated by Django 2.2 on 2020-08-30 10:17

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0019_auto_20200610_1245'),
    ]

    operations = [
        migrations.AddField(
            model_name='moogtmedauser',
            name='blocker',
            field=models.ManyToManyField(related_name='blockings', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='moogtmedauser',
            name='blocking',
            field=models.ManyToManyField(related_name='blockers', to=settings.AUTH_USER_MODEL),
        ),
    ]
