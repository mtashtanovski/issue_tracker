# Generated by Django 4.0.1 on 2022-02-01 15:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0005_projectmodel'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='projectmodel',
            options={'verbose_name': 'Проект', 'verbose_name_plural': 'Проекты'},
        ),
        migrations.AlterModelTable(
            name='projectmodel',
            table='projects',
        ),
    ]