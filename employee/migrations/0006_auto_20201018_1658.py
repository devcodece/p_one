# Generated by Django 2.2 on 2020-10-18 16:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0005_auto_20201018_1549'),
    ]

    operations = [
        migrations.RenameField(
            model_name='skills',
            old_name='skill_name',
            new_name='skill',
        ),
    ]
