# Generated by Django 2.1.15 on 2024-07-18 15:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clinico', '0020_productosnutricion'),
        ('facturacion', '0003_tipossuministro'),
    ]

    operations = [
        migrations.CreateModel(
            name='Suministros',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, max_length=30, null=True)),
                ('nombreGenerico', models.CharField(default='A', editable=False, max_length=250)),
                ('fraccion', models.DecimalField(decimal_places=2, max_digits=20)),
                ('unidadFraccion', models.CharField(blank=True, max_length=20, null=True)),
                ('vence', models.CharField(blank=True, max_length=1, null=True)),
                ('control', models.CharField(blank=True, max_length=1, null=True)),
                ('antibiotico', models.CharField(blank=True, max_length=1, null=True)),
                ('pos', models.CharField(blank=True, max_length=1, null=True)),
                ('facturable', models.CharField(blank=True, max_length=1, null=True)),
                ('stockMinimo', models.DecimalField(decimal_places=2, max_digits=20)),
                ('stockMaximo', models.DecimalField(decimal_places=2, max_digits=20)),
                ('maxOrdenar', models.DecimalField(decimal_places=2, max_digits=20)),
                ('estabilidad', models.DecimalField(decimal_places=0, max_digits=20)),
                ('invFarmacia', models.CharField(blank=True, max_length=1, null=True)),
                ('invAlmacen', models.CharField(blank=True, max_length=1, null=True)),
                ('enfermeria', models.CharField(blank=True, max_length=1, null=True)),
                ('terapia', models.CharField(blank=True, max_length=1, null=True)),
                ('nutricion', models.CharField(blank=True, max_length=1, null=True)),
                ('cantidad', models.DecimalField(decimal_places=2, max_digits=20)),
                ('cums', models.CharField(blank=True, max_length=30, null=True)),
                ('formaFarmaceutica', models.CharField(blank=True, max_length=250, null=True)),
                ('regSanitario', models.CharField(blank=True, max_length=30, null=True)),
                ('altoCosto', models.CharField(blank=True, max_length=1, null=True)),
                ('vrCompra', models.DecimalField(decimal_places=2, max_digits=20)),
                ('vrUltimaCompra', models.DecimalField(decimal_places=2, max_digits=20)),
                ('codigoAtc', models.CharField(blank=True, max_length=10, null=True)),
                ('infusion', models.CharField(blank=True, max_length=1, null=True)),
                ('tipoAdministracion', models.CharField(blank=True, max_length=20, null=True)),
                ('regulado', models.CharField(blank=True, max_length=1, null=True)),
                ('vaorRegulado', models.DecimalField(decimal_places=2, max_digits=20)),
                ('observaciones', models.CharField(blank=True, max_length=250, null=True)),
                ('sispro', models.CharField(blank=True, max_length=1, null=True)),
                ('oncologico', models.CharField(blank=True, max_length=1, null=True)),
                ('ortesis', models.CharField(blank=True, max_length=1, null=True)),
                ('mipres', models.CharField(blank=True, max_length=15, null=True)),
                ('epiHigiene', models.CharField(blank=True, max_length=1, null=True)),
                ('controlStock', models.CharField(blank=True, max_length=1, null=True)),
                ('AnatoPos', models.CharField(blank=True, max_length=1, null=True)),
                ('magistralControl', models.CharField(blank=True, max_length=1, null=True)),
                ('genericoPos', models.CharField(blank=True, max_length=1, null=True)),
                ('fechaRegistro', models.DateTimeField(blank=True, null=True)),
                ('estadoReg', models.CharField(default='A', editable=False, max_length=1)),
                ('concentracion', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='clinico.MedicamentosDci')),
                ('concepto', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='facturacion.Conceptos')),
                ('grupo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='clinico.Grupos')),
                ('subGrupo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='Subgrupo01i01', to='clinico.Grupos')),
                ('tipoSuministro', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='facturacion.TiposSuministro')),
                ('unidadMedida', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='clinico.UnidadesDeMedidaDosis')),
                ('viaAdministracion', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='clinico.ViasAdministracion')),
            ],
        ),
    ]
