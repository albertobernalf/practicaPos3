# Generated by Django 2.1.15 on 2024-09-30 08:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('facturacion', '0033_auto_20240930_0851'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tarifassuministros',
            name='concepto',
        ),
        migrations.RemoveField(
            model_name='tarifassuministros',
            name='suministro',
        ),
        migrations.RemoveField(
            model_name='tarifassuministros',
            name='tipoTarifa',
        ),
        migrations.RemoveField(
            model_name='tarifassuministros',
            name='usuarioRegistro',
        ),
        migrations.DeleteModel(
            name='TarifasSuministros',
        ),
    ]
