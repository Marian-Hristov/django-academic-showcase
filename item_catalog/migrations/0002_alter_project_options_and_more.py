# Generated by Django 4.0.3 on 2022-05-12 19:09

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_management', '0003_alter_profile_options'),
        ('item_catalog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'permissions': [('administrate_projects', 'Can administrate project')]},
        ),
        migrations.RenameField(
            model_name='project',
            old_name='type',
            new_name='project_type',
        ),
        migrations.AlterField(
            model_name='post',
            name='likes',
            field=models.ManyToManyField(blank=True, default=[0], related_name='post_like', to='user_management.profile'),
        ),
        migrations.AlterField(
            model_name='project',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_management.profile'),
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating_value', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)])),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_management.profile')),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='ratings',
            field=models.ManyToManyField(blank=True, default=[0], related_name='post_rating', to='item_catalog.rating'),
        ),
    ]
