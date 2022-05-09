# Generated by Django 4.0.3 on 2022-05-09 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item_catalog', '0008_alter_post_ratings'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='ratings',
            field=models.ManyToManyField(blank=True, default=[0], related_name='post_rating', to='item_catalog.rating'),
        ),
    ]
