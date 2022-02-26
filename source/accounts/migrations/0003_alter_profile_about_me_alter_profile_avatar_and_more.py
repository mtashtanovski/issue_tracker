# Generated by Django 4.0.1 on 2022-02-26 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_profile_about_me_profile_git_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='about_me',
            field=models.TextField(blank=True, max_length=2000, null=True, verbose_name='О себе'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='avatars/', verbose_name='Аватар'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='git_profile',
            field=models.URLField(blank=True, max_length=128, null=True, verbose_name='Профиль GitHub'),
        ),
    ]
