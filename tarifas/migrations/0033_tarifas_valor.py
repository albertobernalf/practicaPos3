# Generated by Django 2.1.15 on 2024-10-28 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tarifas', '0032_auto_20241023_1623'),
    ]

    operations = [
        migrations.AddField(
            model_name='tarifas',
            name='valor',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True),
        ),
    ]
