# Generated by Django 2.1.15 on 2024-09-27 12:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('facturacion', '0029_liquidacioncirugias_tipo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='suministros',
            name='cums',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='rips.RipsCums'),
        ),
        migrations.AlterField(
            model_name='suministros',
            name='formasFarmaceutica',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='rips.RipsFormaFarmaceutica'),
        ),
        migrations.AlterField(
            model_name='suministros',
            name='unidadMedida',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='rips.RipsUmm'),
        ),
    ]
