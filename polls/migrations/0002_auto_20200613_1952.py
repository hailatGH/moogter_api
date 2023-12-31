# Generated by Django 2.1.3 on 2020-06-13 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='poll',
            name='tags',
            field=models.ManyToManyField(blank=True, to='api.Tag'),
        ),
        migrations.AddField(
            model_name='poll',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='poll',
            name='visibility',
            field=models.CharField(choices=[('PUBLIC', 'To the public'), ('FOLLOWERS_ONLY', 'To my subscribers only')], default='PUBLIC', max_length=15),
        ),
    ]
