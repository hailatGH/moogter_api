# Generated by Django 2.2 on 2021-01-28 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arguments', '0012_auto_20201220_1006'),
    ]

    operations = [
        migrations.AddField(
            model_name='argument',
            name='consecutive_expired_turns_count',
            field=models.IntegerField(default=1),
        ),
    ]