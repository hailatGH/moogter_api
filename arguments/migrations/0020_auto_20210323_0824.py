# Generated by Django 2.2 on 2021-03-23 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arguments', '0019_argumentscore'),
    ]

    operations = [
        migrations.AlterField(
            model_name='argument',
            name='argument',
            field=models.CharField(max_length=560),
        ),
    ]
