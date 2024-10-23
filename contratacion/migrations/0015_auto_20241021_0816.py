# Generated by Django 2.1.15 on 2024-10-21 08:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('planta', '0003_auto_20240702_1521'),
        ('tarifas', '0025_liquidaciontarifas'),
        ('contratacion', '0014_auto_20241018_0816'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConveniosLiquidacionTarifas',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('valorNeto', models.DecimalField(blank=True, decimal_places=4, max_digits=15, null=True)),
                ('fechaRegistro', models.DateTimeField(blank=True, null=True)),
                ('estadoReg', models.CharField(default='A', editable=False, max_length=1)),
                ('convenio', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='contratacion.Convenios')),
                ('liquidacionTarifa', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='liqtar101', to='tarifas.LiquidacionTarifas')),
                ('usuarioRegistro', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='plantas213', to='planta.Planta')),
            ],
        ),
        migrations.RemoveField(
            model_name='conveniosliquidacionhonorarios',
            name='liquidacionHonorario',
        ),
        migrations.AddField(
            model_name='conveniosliquidacionhonorarios',
            name='liquidacionTarifa',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='liqtar10', to='tarifas.LiquidacionTarifas'),
        ),
    ]
