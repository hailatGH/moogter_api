# Generated by Django 2.2 on 2020-09-30 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moogts', '0004_moogtminisuggestion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moogtminisuggestion',
            name='state',
            field=models.CharField(choices=[('PENDING', 'Pending'), ('APPROVED', 'Approved'), ('DISAPPROVED', 'Disapproved')], default='Pending', max_length=15),
        ),
    ]