# Generated by Django 2.2 on 2021-05-18 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0007_auto_20210426_1333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='type',
            field=models.CharField(choices=[('moogt_status', 'moogt_status'), ('moogt_request', 'moogt_request'), ('moogt_request_resolved', 'moogt_request_resolved'), ('moogt_card', 'moogt_card'), ('moogt_follow', 'moogt_follow'), ('moogt_premiere', 'moogt_premiere'), ('moogt_conclude', 'moogt_conclude'), ('regular_message', 'regular_message'), ('invitation_message', 'invitation_message'), ('mini_suggestion_message', 'mini_suggestion_message')], default='normal', max_length=20),
        ),
    ]