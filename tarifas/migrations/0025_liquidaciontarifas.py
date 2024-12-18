# Generated by Django 2.1.15 on 2024-10-21 07:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clinico', '0092_examenes_uvraño'),
        ('facturacion', '0052_remove_conceptos_tipocups'),
        ('planta', '0003_auto_20240702_1521'),
        ('tarifas', '0024_auto_20241021_0747'),
    ]

    operations = [
        migrations.CreateModel(
            name='LiquidacionTarifas',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('codigoHomologado', models.CharField(blank=True, max_length=10, null=True)),
                ('descripcion', models.CharField(blank=True, max_length=100, null=True)),
                ('salMinLeg', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('cantidadUvr', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('valorIss', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('valorSoat', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('valorPropio', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('fechaRegistro', models.DateTimeField(blank=True, null=True)),
                ('estadoReg', models.CharField(default='A', editable=False, max_length=1)),
                ('codigoCups', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='Cups1172', to='clinico.Examenes')),
                ('codigoSuministro', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='Suminis1272', to='facturacion.Suministros')),
                ('salariosMinimosLegales', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='MinLeg0112', to='facturacion.SalariosMinimosLegales')),
                ('tipoHonorario', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='TipoHonorario012', to='tarifas.TiposHonorarios')),
                ('tipoTarifa', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='TipoTarifa032', to='tarifas.TiposTarifa')),
                ('usuarioRegistro', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='plantas2172', to='planta.Planta')),
                ('uvrAño', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='Uvr1032', to='tarifas.Uvr')),
            ],
        ),
    ]
