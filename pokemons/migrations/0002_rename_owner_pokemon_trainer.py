# Generated by Django 4.1.2 on 2022-10-30 16:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pokemons', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pokemon',
            old_name='owner',
            new_name='trainer',
        ),
    ]
