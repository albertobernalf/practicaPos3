# Generated by Django 2.1.15 on 2024-09-16 16:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('facturacion', '0018_auto_20240916_1614'),
    ]

    operations = [
        migrations.AddField(
            model_name='liquidacionhonorarios',
            name='salariosMinimosLegales',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='facturacion.SalariosMinimosLegales'),
        ),
    ]