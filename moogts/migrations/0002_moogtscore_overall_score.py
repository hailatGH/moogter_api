# Generated by Django 2.2 on 2020-07-31 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moogts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='moogtscore',
            name='overall_score',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=11),
        ),
    ]