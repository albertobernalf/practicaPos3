# Generated by Django 2.1.15 on 2024-07-11 12:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('facturacion', '0001_initial'),
        ('clinico', '0012_ips'),
        ('admisiones', '0011_auto_20240711_1204'),
    ]

    operations = [
        migrations.AddField(
            model_name='ingresos',
            name='empresa',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='facturacion.Empresas'),
        ),
        migrations.AddField(
            model_name='ingresos',
            name='ipsRemite',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='clinico.Ips'),
        ),
        migrations.AddField(
            model_name='ingresos',
            name='numManilla',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='ingresos',
            name='remitido',
            field=models.CharField(blank=True, max_length=1, null=True),
        ),
    ]
