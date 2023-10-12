# Generated by Django 2.2 on 2020-06-10 12:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('moogts', '0001_initial'),
        ('users', '0018_auto_20200105_0003'),
    ]

    operations = [
        migrations.AddField(
            model_name='moogtmedauser',
            name='bio',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='moogtmedauser',
            name='cover',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='moogtmedauser',
            name='following_moogts',
            field=models.ManyToManyField(related_name='followers', to='moogts.Moogt'),
        ),
        migrations.AddField(
            model_name='moogtmedauser',
            name='last_opened_following_moogt',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='moogts.Moogt'),
        ),
        migrations.AddField(
            model_name='moogtmedauser',
            name='last_opened_moogt',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='moogts.Moogt'),
        ),
        migrations.AddField(
            model_name='moogtmedauser',
            name='quote',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='activity',
            name='type',
            field=models.CharField(choices=[('create_moogt', 'Create Moogt'), ('create_argument', 'Create Argument'), ('follow_user', 'Follow User'), ('unfollow_user', 'Unfollow user'), ('view_moogt', 'View Moogt'), ('follow_moogt', 'Follow Moogt'), ('view_proposition_moogt', 'View Proposition Moogt'), ('view_opposition_moogt', 'View Opposition Moogt'), ('make_comment', 'Make Comment'), ('upvote_argument', 'Upvote Argument'), ('downvote_argument', 'Downvote Argument')], max_length=25),
        ),
        migrations.AlterField(
            model_name='creditpoint',
            name='type',
            field=models.CharField(choices=[('create_moogt', 'Create Moogt'), ('create_argument', 'Create Argument'), ('follow_user', 'Follow User'), ('unfollow_user', 'Unfollow user'), ('view_moogt', 'View Moogt'), ('follow_moogt', 'Follow Moogt'), ('view_proposition_moogt', 'View Proposition Moogt'), ('view_opposition_moogt', 'View Opposition Moogt'), ('make_comment', 'Make Comment'), ('upvote_argument', 'Upvote Argument'), ('downvote_argument', 'Downvote Argument')], default='', max_length=25),
        ),
    ]