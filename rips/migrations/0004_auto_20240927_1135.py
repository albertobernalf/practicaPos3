# Generated by Django 2.1.15 on 2024-09-27 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rips', '0003_auto_20240927_1102'),
    ]

    operations = [
        migrations.AddField(
            model_name='ripsumm',
            name='descripcion',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name='ripsumm',
            name='codigo',
            field=models.CharField(blank=True, max_length=4, null=True),
        ),
    ]