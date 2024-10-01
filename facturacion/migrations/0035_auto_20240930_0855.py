# Generated by Django 2.1.15 on 2024-09-30 08:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clinico', '0086_auto_20240930_0855'),
        ('facturacion', '0034_auto_20240930_0852'),
    ]

    operations = [
        migrations.AlterField(
            model_name='liquidacionderechos',
            name='grupoQx',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='tarifas.GruposQx'),
        ),
        migrations.AlterField(
            model_name='liquidacionhonorarios',
            name='grupoQx',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='tarifas.GruposQx'),
        ),
        migrations.DeleteModel(
            name='GruposQx',
        ),
    ]
