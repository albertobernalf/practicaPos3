# Generated by Django 2.1.15 on 2024-09-17 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facturacion', '0024_liquidacioncirugias'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uvr',
            name='valor',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=15, null=True),
        ),
    ]