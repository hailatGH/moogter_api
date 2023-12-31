# Generated by Django 2.2 on 2020-06-10 12:45

import annoying.fields
import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Poll',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=280)),
                ('start_date', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
                ('end_date', models.DateTimeField(blank=True, default=None, null=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('max_duration', models.DurationField(default=datetime.timedelta(days=1))),
                ('visibility', models.CharField(choices=[('PUBLIC', 'To the public'), ('FOLLOWERS_ONLY', 'To my subscribers only')], max_length=25)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='polls', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PollScore',
            fields=[
                ('score_now', models.DecimalField(decimal_places=2, default=0, max_digits=11)),
                ('score_before', models.DecimalField(decimal_places=2, default=0, max_digits=11)),
                ('score_last_updated_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('poll', annoying.fields.AutoOneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='score', serialize=False, to='polls.Poll')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PollStats',
            fields=[
                ('poll', annoying.fields.AutoOneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='stats', serialize=False, to='polls.Poll')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PollOption',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=50)),
                ('poll', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='options', to='polls.Poll')),
                ('votes', models.ManyToManyField(blank=True, related_name='_polloption_votes_+', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
