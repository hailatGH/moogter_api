# Generated by Django 2.2 on 2020-12-01 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moogts', '0012_moogtactivity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moogtactivity',
            name='type',
            field=models.CharField(choices=[('CARD_REQUEST', 'CARD_REQUEST')], default=None, max_length=15, null=True),
        ),
    ]
