# Generated by Django 2.2 on 2020-07-31 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20200613_1952'),
    ]

    operations = [
        migrations.AddField(
            model_name='pollscore',
            name='overall_score',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=11),
        ),
    ]