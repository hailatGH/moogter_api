# Generated by Django 2.2 on 2020-11-09 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invitations', '0004_invitation_parent_invitation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invitation',
            name='status',
            field=models.CharField(choices=[('PENDING', 'Pending'), ('ACCEPTED', 'Accepted'), ('DECLINED', 'Declined'), ('CANCELLED', 'Cancelled'), ('EDITED', 'EDITED'), ('REVISED', 'REVISED'), ('START_ANYTIME_INVITER', 'START_ANYTIME_INVITER'), ('START_ANYTIME_INVITEE', 'START_ANYTIME_INVITEE'), ('ACCEPTED_START_ANYTIME_INVITER', 'ACCEPTED_START_ANYTIME_INVITER'), ('ACCEPTED_START_ANYTIME_INVITEE', 'ACCEPTED_START_ANYTIME_INVITEE'), ('STARTED', 'STARTED')], default='PENDING', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='moderatorsuggestion',
            name='status',
            field=models.CharField(choices=[('PENDING', 'Pending'), ('ACCEPTED', 'Accepted'), ('DECLINED', 'Declined'), ('CANCELLED', 'Cancelled'), ('EDITED', 'EDITED'), ('REVISED', 'REVISED'), ('START_ANYTIME_INVITER', 'START_ANYTIME_INVITER'), ('START_ANYTIME_INVITEE', 'START_ANYTIME_INVITEE'), ('ACCEPTED_START_ANYTIME_INVITER', 'ACCEPTED_START_ANYTIME_INVITER'), ('ACCEPTED_START_ANYTIME_INVITEE', 'ACCEPTED_START_ANYTIME_INVITEE'), ('STARTED', 'STARTED')], default='PENDING', max_length=50),
        ),
    ]
