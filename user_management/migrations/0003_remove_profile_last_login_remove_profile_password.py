# Generated by Django 4.0.4 on 2022-04-25 14:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_management', '0002_delete_imagefile_profile_avatar_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='last_login',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='password',
        ),
    ]