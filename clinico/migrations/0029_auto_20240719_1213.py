# Generated by Django 2.1.15 on 2024-07-19 12:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0003_auto_20240710_1531'),
        ('clinico', '0028_medicamentos'),
    ]

    operations = [
        migrations.CreateModel(
            name='TiposEvolucion',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=30)),
                ('estadoReg', models.CharField(default='A', editable=False, max_length=1)),
            ],
        ),
        migrations.AddField(
            model_name='historia',
            name='antibioticos',
            field=models.CharField(blank=True, max_length=1),
        ),
        migrations.AddField(
            model_name='historia',
            name='apache2',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='historia',
            name='enfermedadActual',
            field=models.CharField(blank=True, max_length=5000),
        ),
        migrations.AddField(
            model_name='historia',
            name='epicrisis',
            field=models.CharField(blank=True, max_length=20000),
        ),
        migrations.AddField(
            model_name='historia',
            name='examenFisico',
            field=models.CharField(blank=True, max_length=5000),
        ),
        migrations.AddField(
            model_name='historia',
            name='fecNotaAclaratoria',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='historia',
            name='hipotension',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='historia',
            name='indiceMortalidad',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='historia',
            name='ingestaAlcohol',
            field=models.CharField(blank=True, max_length=5000),
        ),
        migrations.AddField(
            model_name='historia',
            name='inmovilizacion',
            field=models.CharField(blank=True, max_length=1),
        ),
        migrations.AddField(
            model_name='historia',
            name='inmovilizacionObservaciones',
            field=models.CharField(blank=True, max_length=5000),
        ),
        migrations.AddField(
            model_name='historia',
            name='interconsulta',
            field=models.CharField(blank=True, max_length=1),
        ),
        migrations.AddField(
            model_name='historia',
            name='irritacion',
            field=models.CharField(blank=True, max_length=1),
        ),
        migrations.AddField(
            model_name='historia',
            name='justificacion',
            field=models.CharField(blank=True, max_length=5000),
        ),
        migrations.AddField(
            model_name='historia',
            name='leucopenia',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='historia',
            name='llenadoCapilar',
            field=models.CharField(blank=True, max_length=1),
        ),
        migrations.AddField(
            model_name='historia',
            name='manejoQx',
            field=models.CharField(blank=True, max_length=20000),
        ),
        migrations.AddField(
            model_name='historia',
            name='monitoreo',
            field=models.CharField(blank=True, max_length=1),
        ),
        migrations.AddField(
            model_name='historia',
            name='movilidadLimitada',
            field=models.CharField(blank=True, max_length=1),
        ),
        migrations.AddField(
            model_name='historia',
            name='nauseas',
            field=models.CharField(blank=True, max_length=1),
        ),
        migrations.AddField(
            model_name='historia',
            name='neurologia',
            field=models.CharField(blank=True, max_length=1),
        ),
        migrations.AddField(
            model_name='historia',
            name='noQx',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name='historia',
            name='notaAclaratoria',
            field=models.CharField(blank=True, max_length=1),
        ),
        migrations.AddField(
            model_name='historia',
            name='observaciones',
            field=models.CharField(blank=True, max_length=5000),
        ),
        migrations.AddField(
            model_name='historia',
            name='pulsos',
            field=models.CharField(blank=True, max_length=1),
        ),
        migrations.AddField(
            model_name='historia',
            name='retiroPuntos',
            field=models.CharField(blank=True, max_length=1),
        ),
        migrations.AddField(
            model_name='historia',
            name='riesgoHemodinamico',
            field=models.CharField(blank=True, max_length=15),
        ),
        migrations.AddField(
            model_name='historia',
            name='riesgoVentilatorio',
            field=models.CharField(blank=True, max_length=15),
        ),
        migrations.AddField(
            model_name='historia',
            name='riesgos',
            field=models.CharField(blank=True, max_length=5000),
        ),
        migrations.AddField(
            model_name='historia',
            name='textoNotaAclaratoria',
            field=models.CharField(blank=True, max_length=5000),
        ),
        migrations.AddField(
            model_name='historia',
            name='tratamiento',
            field=models.CharField(blank=True, max_length=5000),
        ),
        migrations.AddField(
            model_name='historia',
            name='trombocitopenia',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='historia',
            name='usuarioNotaAclaratoria',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='usuarios.Usuarios'),
        ),
        migrations.AddField(
            model_name='historia',
            name='vomito',
            field=models.CharField(blank=True, max_length=1),
        ),
        migrations.AlterField(
            model_name='historia',
            name='causasExterna',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='clinico.CausasExterna'),
        ),
        migrations.AlterField(
            model_name='historia',
            name='dependenciasRealizado',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='sitios.Dependencias'),
        ),
        migrations.AlterField(
            model_name='historia',
            name='documento',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='DocumentoHistoria5672', to='usuarios.Usuarios'),
        ),
        migrations.AlterField(
            model_name='historia',
            name='especialidades',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='clinico.Especialidades'),
        ),
        migrations.AlterField(
            model_name='historia',
            name='fechaRegistro',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='historia',
            name='planta',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='planta.Planta'),
        ),
        migrations.AlterField(
            model_name='historia',
            name='tipoDoc',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='usuarios.TiposDocumento'),
        ),
        migrations.AlterField(
            model_name='historia',
            name='tiposFolio',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='clinico.TiposFolio'),
        ),
        migrations.AlterField(
            model_name='historia',
            name='usuarioRegistro',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='lanta345', to='planta.Planta'),
        ),
        migrations.AddField(
            model_name='historia',
            name='tipoEvolucion',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='clinico.TiposEvolucion'),
        ),
    ]
