# Generated by Django 2.1.15 on 2024-10-29 07:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clinico', '0096_auto_20241023_1432'),
        ('facturacion', '0054_auto_20241023_1529'),
        ('tarifas', '0033_tarifas_valor'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='honorariosiss',
            unique_together={('tipoTarifa', 'tipoHonorario')},
        ),
        migrations.AlterUniqueTogether(
            name='honorariossoat',
            unique_together={('tipoTarifa', 'tipoHonorario')},
        ),
        migrations.AlterUniqueTogether(
            name='liquidaciontarifashonorarios',
            unique_together={('tipoTarifa', 'tipoHonorario')},
        ),
        migrations.AlterUniqueTogether(
            name='tarifas',
            unique_together={('tipoTarifa', 'codigoCups')},
        ),
        migrations.AlterUniqueTogether(
            name='tarifassuministros',
            unique_together={('tipoTarifa', 'suministro')},
        ),
    ]
