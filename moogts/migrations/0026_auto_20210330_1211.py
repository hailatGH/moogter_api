# Generated by Django 2.2 on 2021-03-30 12:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('moogts', '0025_auto_20210216_1206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moogtactivity',
            name='status',
            field=models.CharField(choices=[('Pending', 'PENDING'), ('Accepted', 'ACCEPTED'), ('Declined', 'DECLINED'), ('Cancelled', 'CANCELLED'), ('Expired', 'EXPIRED')], default='Pending', max_length=15),
        ),
        migrations.AlterField(
            model_name='moogtactivity',
            name='type',
            field=models.CharField(choices=[('CARD_REQUEST', 'CARD_REQUEST'), ('END_REQUEST', 'END_REQUEST'), ('PAUSE_REQUEST', 'PAUSE_REQUEST'), ('RESUME_REQUEST', 'RESUME_REQUEST'), ('DELETE_REQUEST', 'DELETE_REQUEST'), ('ENDORSEMENT', 'ENDORSEMENT'), ('DISAGREEMENT', 'DISAGREEMENT')], default=None, max_length=15, null=True),
        ),
        migrations.CreateModel(
            name='MoogtStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True, null=True)),
                ('updated_at', models.DateTimeField(blank=True, db_index=True, null=True)),
                ('status', models.CharField(choices=[('started', 'started'), ('paused', 'paused'), ('auto_paused', 'auto_paused'), ('paused', 'paused'), ('resumed', 'resumed'), ('broke_off', 'broke_off'), ('ended', 'ended'), ('duration_over', 'duration_over')], max_length=20)),
                ('moogt', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='statuses', to='moogts.Moogt')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
