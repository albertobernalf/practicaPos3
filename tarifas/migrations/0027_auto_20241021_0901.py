# Generated by Django 2.1.15 on 2024-10-21 09:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('facturacion', '0052_remove_conceptos_tipocups'),
        ('contratacion', '0016_auto_20241021_0828'),
        ('planta', '0003_auto_20240702_1521'),
        ('clinico', '0092_examenes_uvraño'),
        ('tarifas', '0026_auto_20241021_0857'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='LiquidacionTarifas',
            new_name='LiquidacionTarifasHonorarios',
        ),
    ]