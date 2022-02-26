# Generated by Django 4.0.1 on 2022-02-26 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='about_me',
            field=models.TextField(max_length=2000, null=True, verbose_name='О себе'),
        ),
        migrations.AddField(
            model_name='profile',
            name='git_profile',
            field=models.URLField(max_length=128, null=True, verbose_name='Профиль GitHub'),
        ),
    ]