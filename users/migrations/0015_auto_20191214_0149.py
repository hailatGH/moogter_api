# Generated by Django 2.1.3 on 2019-12-14 01:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0014_creditpoint_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='type',
            field=models.CharField(choices=[('create_moogt', 'Create Moogt'), ('create_argument', 'Create Argument'), ('follow_user', 'Follow User'), ('view_moogt', 'View Moogt'), ('view_proposition_moogt', 'View Proposition Moogt'), ('view_opposition_moogt', 'View Opposition Moogt'), ('make_comment', 'Make Comment'), ('upvote_argument', 'Upvote Argument'), ('downvote_argument', 'Downvote Argument')], max_length=25),
        ),
        migrations.AlterField(
            model_name='creditpoint',
            name='type',
            field=models.CharField(choices=[('create_moogt', 'Create Moogt'), ('create_argument', 'Create Argument'), ('follow_user', 'Follow User'), ('view_moogt', 'View Moogt'), ('view_proposition_moogt', 'View Proposition Moogt'), ('view_opposition_moogt', 'View Opposition Moogt'), ('make_comment', 'Make Comment'), ('upvote_argument', 'Upvote Argument'), ('downvote_argument', 'Downvote Argument')], default='', max_length=25),
        ),
    ]