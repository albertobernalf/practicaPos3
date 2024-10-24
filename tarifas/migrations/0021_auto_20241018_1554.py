# Generated by Django 2.1.15 on 2024-10-18 15:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('facturacion', '0051_auto_20241018_0959'),
        ('tarifas', '0020_auto_20241018_0854'),
    ]

    operations = [
        migrations.AddField(
            model_name='tarifas',
            name='salMinLeg',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True),
        ),
        migrations.AddField(
            model_name='tarifas',
            name='salariosMinimosLegales',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='MinLeg01', to='facturacion.SalariosMinimosLegales'),
        ),
        migrations.AlterField(
            model_name='liquidacionhonorarios',
            name='salariosMinimosLegales',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='MinLeg011', to='facturacion.SalariosMinimosLegales'),
        ),
    ]