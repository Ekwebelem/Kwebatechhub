# Generated by Django 4.2.2 on 2023-09-01 12:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_contactsubmission_alter_jobapplication_email'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='firstname',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='lastname',
            new_name='last_name',
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='phoneno',
            new_name='phone_number',
        ),
    ]
