# Generated by Django 2.1.15 on 2024-09-27 10:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rips', '0001_initial'),
        ('admisiones', '0018_auto_20240926_0741'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ingresos',
            old_name='DestinoUsuarioEgresoRecienNacido',
            new_name='ripsDestinoUsuarioEgresoRecienNacido',
        ),
        migrations.RenameField(
            model_name='ingresos',
            old_name='edadGestacional',
            new_name='ripsEdadGestacional',
        ),
        migrations.RenameField(
            model_name='ingresos',
            old_name='numConsultasCPrenatal',
            new_name='ripsNumConsultasCPrenatal',
        ),
        migrations.RenameField(
            model_name='ingresos',
            old_name='pesoRecienNacido',
            new_name='ripsPesoRecienNacido',
        ),
        migrations.RenameField(
            model_name='ingresos',
            old_name='recienNacido',
            new_name='ripsRecienNacido',
        ),
        migrations.AddField(
            model_name='ingresos',
            name='ripsCausaMotivoAtencion',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='rips.RipsCausaExterna'),
        ),
        migrations.AddField(
            model_name='ingresos',
            name='ripsCodServicio',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='rips.RipsServicios'),
        ),
        migrations.AddField(
            model_name='ingresos',
            name='ripsCondicionDestinoUsuarioEgreso',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='rips.RipsDestinoEgreso'),
        ),
        migrations.AddField(
            model_name='ingresos',
            name='ripsGrupoServicios',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='rips.RipsGrupoServicios'),
        ),
        migrations.AddField(
            model_name='ingresos',
            name='ripsViaIngresoServicioSalud',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='rips.RipsViasIngresoSalud'),
        ),
        migrations.AddField(
            model_name='ingresos',
            name='ripsmodalidadGrupoServicioTecSal',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='rips.RipsModalidadAtencion'),
        ),
    ]