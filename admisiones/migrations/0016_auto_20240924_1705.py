# Generated by Django 2.1.15 on 2024-09-24 17:05

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('planta', '0003_auto_20240702_1521'),
        ('clinico', '0078_auto_20240919_0931'),
        ('sitios', '0012_auto_20240812_1010'),
        ('usuarios', '0005_auto_20240919_1605'),
        ('admisiones', '0015_alter_furips_estadoreg'),
    ]

    operations = [
        migrations.RenameField(
            model_name='furips',
            old_name='documentoConductor',
            new_name='cobroExcedentePoliza',
        ),
        migrations.RenameField(
            model_name='furips',
            old_name='documentoPlaca2',
            new_name='codigoInscripcion',
        ),
        migrations.RenameField(
            model_name='furips',
            old_name='documentoPlaca3',
            new_name='codigoInscripcionRecibe',
        ),
        migrations.RenameField(
            model_name='furips',
            old_name='consec',
            new_name='consecVictima',
        ),
        migrations.RenameField(
            model_name='furips',
            old_name='direccionConductor',
            new_name='direccionInvolucrado',
        ),
        migrations.RenameField(
            model_name='furips',
            old_name='direccionProietario',
            new_name='direccionPropietario',
        ),
        migrations.RenameField(
            model_name='furips',
            old_name='estadoAsegurado',
            new_name='documentoInvolucrado',
        ),
        migrations.RenameField(
            model_name='furips',
            old_name='documentoProfesional',
            new_name='documentoProfesionalAtendio',
        ),
        migrations.RenameField(
            model_name='furips',
            old_name='direccionVictima',
            new_name='lugarRecogeVictima',
        ),
        migrations.RenameField(
            model_name='furips',
            old_name='dispositivoSeguridad',
            new_name='marcaVehiculo',
        ),
        migrations.RenameField(
            model_name='furips',
            old_name='poliza',
            new_name='numeroPlacaTranporto',
        ),
        migrations.RenameField(
            model_name='furips',
            old_name='radicadoSiras',
            new_name='numeroPoliza',
        ),
        migrations.RenameField(
            model_name='furips',
            old_name='apellidosConductor',
            new_name='numeroRadicacion',
        ),
        migrations.RenameField(
            model_name='furips',
            old_name='apellidosPropietario',
            new_name='numeroRadicadoAnterior',
        ),
        migrations.RenameField(
            model_name='furips',
            old_name='telefonoConductor',
            new_name='placaVehiculo',
        ),
        migrations.RenameField(
            model_name='furips',
            old_name='telefonoPropietario',
            new_name='primerApellidoInvolucrado',
        ),
        migrations.RenameField(
            model_name='furips',
            old_name='tipoAutomotor',
            new_name='primerApellidoPropietario',
        ),
        migrations.RenameField(
            model_name='furips',
            old_name='tipoColision',
            new_name='primerApellidoVictima',
        ),
        migrations.RenameField(
            model_name='furips',
            old_name='tipoDocPlaca2',
            new_name='tipoDocVictima',
        ),
        migrations.RemoveField(
            model_name='furips',
            name='accidenteMultiple',
        ),
        migrations.RemoveField(
            model_name='furips',
            name='completo',
        ),
        migrations.RemoveField(
            model_name='furips',
            name='documento',
        ),
        migrations.RemoveField(
            model_name='furips',
            name='ingresoUci',
        ),
        migrations.RemoveField(
            model_name='furips',
            name='marcaAsegurado',
        ),
        migrations.RemoveField(
            model_name='furips',
            name='municipioconductor',
        ),
        migrations.RemoveField(
            model_name='furips',
            name='nombresConductor',
        ),
        migrations.RemoveField(
            model_name='furips',
            name='nombresPropietario',
        ),
        migrations.RemoveField(
            model_name='furips',
            name='placa2',
        ),
        migrations.RemoveField(
            model_name='furips',
            name='placa3',
        ),
        migrations.RemoveField(
            model_name='furips',
            name='placaAsegurado',
        ),
        migrations.RemoveField(
            model_name='furips',
            name='telVictima',
        ),
        migrations.RemoveField(
            model_name='furips',
            name='tipoDoc',
        ),
        migrations.RemoveField(
            model_name='furips',
            name='tipoDocConductor',
        ),
        migrations.RemoveField(
            model_name='furips',
            name='tipoDocPlaca3',
        ),
        migrations.RemoveField(
            model_name='furips',
            name='tipoDocProfesional',
        ),
        migrations.RemoveField(
            model_name='furips',
            name='velocidadAutomotor',
        ),
        migrations.AddField(
            model_name='furips',
            name='amparoReclamaAFosygaGastos',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=7),
        ),
        migrations.AddField(
            model_name='furips',
            name='amparoReclamaAFosygaQx',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=7),
        ),
        migrations.AddField(
            model_name='furips',
            name='amparoReclamaFacturadoGastos',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=7),
        ),
        migrations.AddField(
            model_name='furips',
            name='amparoReclamaFacturadoQx',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=7),
        ),
        migrations.AddField(
            model_name='furips',
            name='certificacionEgreso',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='furips',
            name='certificacionIngreso',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='furips',
            name='condicionAccidentado',
            field=models.CharField(choices=[('A', 'ACTIVO'), ('I', 'INACTIVO')], default='A', editable=False, max_length=1),
        ),
        migrations.AddField(
            model_name='furips',
            name='departamentoEvento',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='dept10', to='sitios.Departamentos'),
        ),
        migrations.AddField(
            model_name='furips',
            name='departamentoInvolucrado',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='dept12', to='sitios.Departamentos'),
        ),
        migrations.AddField(
            model_name='furips',
            name='departamentoPropietario',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='dept11', to='sitios.Departamentos'),
        ),
        migrations.AddField(
            model_name='furips',
            name='documentoVictima',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='Documento14', to='usuarios.Usuarios'),
        ),
        migrations.AddField(
            model_name='furips',
            name='estado',
            field=models.CharField(blank=True, choices=[('Asegurado', 'Asegurado'), ('No Asegurado', 'No Asegurado'), ('Vehiculo Fantasma', 'Vehiculo Fantasma'), ('Poliza Falsa', 'Poliza Falsa'), ('Vehiculo en fuga', 'Vehiculo en fuga')], max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='furips',
            name='fechaAceptacion',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='furips',
            name='fechaRemision',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True),
        ),
        migrations.AddField(
            model_name='furips',
            name='intervencionAutoridad',
            field=models.CharField(blank=True, max_length=1, null=True),
        ),
        migrations.AddField(
            model_name='furips',
            name='localidadInvolucrado',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='sitios.Localidades'),
        ),
        migrations.AddField(
            model_name='furips',
            name='localidadPropietario',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='local10', to='sitios.Localidades'),
        ),
        migrations.AddField(
            model_name='furips',
            name='municipioInvolucrado',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='muni12', to='sitios.Municipios'),
        ),
        migrations.AddField(
            model_name='furips',
            name='prestadorRecibe',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='ips86', to='clinico.Ips'),
        ),
        migrations.AddField(
            model_name='furips',
            name='prestadorRemite',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='ips7', to='clinico.Ips'),
        ),
        migrations.AddField(
            model_name='furips',
            name='primerNombreInvolucrado',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='furips',
            name='primerNombrePropietario',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='furips',
            name='primerNombreVictima',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='furips',
            name='profesionalRecibe',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='furips',
            name='profesionalRemite',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='planta112', to='planta.Planta'),
        ),
        migrations.AddField(
            model_name='furips',
            name='segundoApellidoInvolucrado',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='furips',
            name='segundoApellidoPropietario',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='furips',
            name='segundoApellidoVictima',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='furips',
            name='segundoNombreInvolucrado',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='furips',
            name='segundoNombrePropietario',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='furips',
            name='segundoNombreVictima',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='furips',
            name='tipoDocInvolucrado',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='tipoDoc15', to='usuarios.TiposDocumento'),
        ),
        migrations.AddField(
            model_name='furips',
            name='tipoDocProfesionalAtendio',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='tipoDoc16', to='usuarios.TiposDocumento'),
        ),
        migrations.AddField(
            model_name='furips',
            name='tipoReferencia',
            field=models.CharField(blank=True, choices=[('Remision', 'Remision'), ('Orden de Servicio', 'Orden de Servicio')], max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='furips',
            name='tipoServicioVehiculo',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='furips',
            name='tipoTransporteTransporto',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
        migrations.AddField(
            model_name='furips',
            name='trasportoVictimaDesde',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
        migrations.AddField(
            model_name='furips',
            name='trasportoVictimaHasta',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
        migrations.AddField(
            model_name='furips',
            name='zonaEvento',
            field=models.CharField(default='A', editable=False, max_length=1),
        ),
        migrations.AlterField(
            model_name='furips',
            name='fechaEvento',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True),
        ),
        migrations.AlterField(
            model_name='furips',
            name='fechaFinPoliza',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True),
        ),
        migrations.AlterField(
            model_name='furips',
            name='fechaIniPoliza',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True),
        ),
        migrations.AlterField(
            model_name='furips',
            name='localidadEvento',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='local09', to='sitios.Localidades'),
        ),
        migrations.AlterField(
            model_name='furips',
            name='municipioEvento',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='muni10', to='sitios.Municipios'),
        ),
        migrations.AlterField(
            model_name='furips',
            name='municipioPropietario',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='muni11', to='sitios.Municipios'),
        ),
        migrations.AlterField(
            model_name='furips',
            name='tipoDocPropietario',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='tipoDoc17', to='usuarios.TiposDocumento'),
        ),
        migrations.AlterField(
            model_name='furips',
            name='tipoVehiculo',
            field=models.CharField(blank=True, choices=[('Servicio Particular', 'Servicio Particular'), ('Servicio Publico', 'Servicio Publico'), ('Servicio Oficial', 'Servicio Oficial'), ('Servicio Diplomatico', 'Servicio Diplomatico'), ('De transporte Masivo', 'De transporte Masivo'), ('Escolar', 'Escolar')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='furips',
            name='usuarioCrea',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='planta111', to='planta.Planta'),
        ),
    ]