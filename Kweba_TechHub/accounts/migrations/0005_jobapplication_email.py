# Generated by Django 4.2.2 on 2023-09-01 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_jobapplication'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobapplication',
            name='email',
            field=models.EmailField(default='barry@kwebaacademy.com', max_length=254),
        ),
    ]
