# Generated by Django 2.2 on 2020-11-13 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moogts', '0009_auto_20201028_0824'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='moogt',
            name='premiering_duration',
        ),
        migrations.AddField(
            model_name='moogt',
            name='premiering_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='moogtminisuggestion',
            name='premiering_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
