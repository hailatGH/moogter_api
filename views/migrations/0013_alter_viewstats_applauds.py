# Generated by Django 4.2.5 on 2023-09-22 09:02

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('views', '0012_auto_20220324_0840'),
    ]

    operations = [
        migrations.AlterField(
            model_name='viewstats',
            name='applauds',
            field=models.ManyToManyField(related_name='+', to=settings.AUTH_USER_MODEL),
        ),
    ]