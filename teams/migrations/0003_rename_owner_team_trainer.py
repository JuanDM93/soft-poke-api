# Generated by Django 4.1.2 on 2022-10-30 16:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0002_team_members'),
    ]

    operations = [
        migrations.RenameField(
            model_name='team',
            old_name='owner',
            new_name='trainer',
        ),
    ]
