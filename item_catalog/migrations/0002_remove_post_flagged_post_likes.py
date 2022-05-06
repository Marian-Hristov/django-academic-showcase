# Generated by Django 4.0.4 on 2022-05-05 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item_catalog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='flagged',
        ),
        migrations.AddField(
            model_name='post',
            name='likes',
            field=models.ManyToManyField(related_name='post_like', to='item_catalog.profile'),
        ),
    ]