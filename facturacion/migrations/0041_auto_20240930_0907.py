# Generated by Django 2.1.15 on 2024-09-30 09:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('facturacion', '0040_auto_20240930_0905'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='liquidacionderechos',
            name='grupoQx',
        ),
        migrations.RemoveField(
            model_name='liquidacionderechos',
            name='salariosMinimosLegales',
        ),
        migrations.RemoveField(
            model_name='liquidacionderechos',
            name='tipoSala',
        ),
        migrations.RemoveField(
            model_name='liquidacionderechos',
            name='tipoTarifa',
        ),
        migrations.DeleteModel(
            name='LiquidacionDerechos',
        ),
    ]
