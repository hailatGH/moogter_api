# Generated by Django 4.2.5 on 2023-09-26 11:05

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moogts', '0039_alter_donation_id_alter_moogt_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='moogt',
            name='numberOfCard',
            field=models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(0, message='Value must be greater than or equal to 0.'), django.core.validators.MaxValueValidator(100, message='Value must be less than or equal to 100.')]),
        ),
    ]
