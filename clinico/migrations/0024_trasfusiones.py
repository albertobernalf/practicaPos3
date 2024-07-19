# Generated by Django 2.1.15 on 2024-07-18 16:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('planta', '0003_auto_20240702_1521'),
        ('usuarios', '0003_auto_20240710_1531'),
        ('clinico', '0023_revisionpacientessistemas'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trasfusiones',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('consecAdmision', models.IntegerField(default=0)),
                ('folio', models.IntegerField(default=0)),
                ('fecha', models.DateTimeField()),
                ('selloCalidad', models.CharField(blank=True, max_length=5000)),
                ('grupoBolsa', models.CharField(blank=True, max_length=50)),
                ('fechaCaducidad', models.DateTimeField()),
                ('realizoTrasfusion', models.CharField(blank=True, max_length=50)),
                ('trasfusionInicio', models.CharField(blank=True, max_length=50)),
                ('trasfusionFinal', models.CharField(blank=True, max_length=50)),
                ('complicaciones', models.CharField(blank=True, max_length=5000)),
                ('tipoComponente', models.CharField(blank=True, max_length=50)),
                ('epicrisis', models.CharField(blank=True, max_length=5000)),
                ('compReactRtha', models.CharField(blank=True, max_length=15)),
                ('compEnfInjerto', models.CharField(blank=True, max_length=15)),
                ('compSobreCargaCirc', models.CharField(blank=True, max_length=15)),
                ('compLesPulmonar', models.CharField(blank=True, max_length=15)),
                ('compReacAlergica', models.CharField(blank=True, max_length=15)),
                ('compSepsis', models.CharField(blank=True, max_length=15)),
                ('compPurpPostTrans', models.CharField(blank=True, max_length=15)),
                ('compReacFHemolitica', models.CharField(blank=True, max_length=15)),
                ('compReacFNoHemolitica', models.CharField(blank=True, max_length=15)),
                ('compEmboAereo', models.CharField(blank=True, max_length=15)),
                ('compHipocalemia', models.CharField(blank=True, max_length=15)),
                ('compHipotermia', models.CharField(blank=True, max_length=15)),
                ('compTransMasiva', models.CharField(blank=True, max_length=15)),
                ('compEscalofrios', models.CharField(blank=True, max_length=15)),
                ('compOtro', models.CharField(blank=True, max_length=15)),
                ('compOtroDesc', models.CharField(blank=True, max_length=2000)),
                ('fechaRegistro', models.DateTimeField(blank=True, null=True)),
                ('estadoReg', models.CharField(default='A', editable=False, max_length=1)),
                ('documento', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='DocumentoHistoria62', to='usuarios.Usuarios')),
                ('tipoDoc', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='usuarios.TiposDocumento')),
                ('usuarioRegistro', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='planta.Planta')),
            ],
        ),
    ]
