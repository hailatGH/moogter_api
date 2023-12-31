# Generated by Django 2.2 on 2020-12-05 08:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('arguments', '0007_auto_20201204_1258'),
    ]

    operations = [
        migrations.AddField(
            model_name='argumentactivity',
            name='actor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='argumentactivity',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, db_index=True, null=True),
        ),
        migrations.AddField(
            model_name='argumentactivity',
            name='updated_at',
            field=models.DateTimeField(blank=True, db_index=True, null=True),
        ),
    ]
