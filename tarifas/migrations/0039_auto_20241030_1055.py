# Generated by Django 2.1.15 on 2024-10-30 10:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tarifas', '0038_auto_20241030_1031'),
    ]

    operations = [
        migrations.RenameField(
            model_name='liquidaciontarifashonorarios',
            old_name='cantidadUvr',
            new_name='valor',
        ),
        migrations.RemoveField(
            model_name='liquidaciontarifashonorarios',
            name='salMinLeg',
        ),
        migrations.RemoveField(
            model_name='liquidaciontarifashonorarios',
            name='salariosMinimosLegales',
        ),
        migrations.RemoveField(
            model_name='liquidaciontarifashonorarios',
            name='uvrAño',
        ),
        migrations.RemoveField(
            model_name='liquidaciontarifashonorarios',
            name='valorIss',
        ),
        migrations.RemoveField(
            model_name='liquidaciontarifashonorarios',
            name='valorPropio',
        ),
        migrations.RemoveField(
            model_name='liquidaciontarifashonorarios',
            name='valorSoat',
        ),
    ]
