# Generated by Django 2.2 on 2020-08-28 10:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chat', '0002_auto_20200826_1809'),
    ]

    operations = [
        migrations.CreateModel(
            name='RegularMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_at', models.DateTimeField(blank=True, db_index=True, null=True)),
                ('content', models.CharField(max_length=560, null=True)),
                ('conversation', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='regular_messages', to='chat.Conversation')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]