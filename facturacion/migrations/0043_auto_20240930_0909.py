# Generated by Django 2.1.15 on 2024-09-30 09:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('facturacion', '0042_auto_20240930_0908'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='formasliquidacion',
            name='usuarioRegistro',
        ),
        migrations.DeleteModel(
            name='FormasLiquidacion',
        ),
    ]