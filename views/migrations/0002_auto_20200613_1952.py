# Generated by Django 2.1.3 on 2020-06-13 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('views', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='view',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='view',
            name='tags',
            field=models.ManyToManyField(blank=True, to='api.Tag'),
        ),
    ]