# Generated by Django 2.1.15 on 2024-10-21 09:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('planta', '0003_auto_20240702_1521'),
        ('tarifas', '0027_auto_20241021_0901'),
        ('contratacion', '0016_auto_20241021_0828'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ConveniosLiquidacionTarifas',
            new_name='ConveniosTarifasHonorarios',
        ),
    ]