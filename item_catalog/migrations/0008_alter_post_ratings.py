# Generated by Django 4.0.4 on 2022-05-08 23:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item_catalog', '0007_post_ratings'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='ratings',
            field=models.ManyToManyField(blank=True, default=[0], null=True, related_name='post_rating', to='item_catalog.rating'),
        ),
    ]
