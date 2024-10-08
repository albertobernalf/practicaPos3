# Generated by Django 2.1.15 on 2024-09-27 15:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cartera', '0007_tiposnotas'),
        ('planta', '0003_auto_20240702_1521'),
        ('clinico', '0085_auto_20240927_1157'),
        ('usuarios', '0005_auto_20240919_1605'),
        ('contratacion', '0006_auto_20240917_0902'),
        ('rips', '0004_auto_20240927_1135'),
        ('facturacion', '0030_auto_20240927_1204'),
    ]

    operations = [
        migrations.CreateModel(
            name='Facturacion',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('documento', models.CharField(blank=True, max_length=30, null=True)),
                ('consecAdmision', models.IntegerField(blank=True, null=True)),
                ('factura', models.CharField(blank=True, max_length=20, null=True)),
                ('fechaFactura', models.DateTimeField(blank=True, null=True)),
                ('codigoDian', models.CharField(blank=True, max_length=30, null=True)),
                ('totalCopagos', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('totalCuotaModeradora', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('totalAbonos', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('totalProcedimientos', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('totalSuministros', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('totalFactura', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('valorApagar', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('valorAPagarLetras', models.CharField(blank=True, max_length=120, null=True)),
                ('anulado', models.CharField(blank=True, max_length=1, null=True)),
                ('fechaCorte', models.DateTimeField(blank=True, null=True)),
                ('cufeDefinitivo', models.CharField(blank=True, max_length=100, null=True)),
                ('cufeValor', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('codigoQr', models.CharField(blank=True, max_length=100, null=True)),
                ('rutaQr', models.CharField(blank=True, max_length=100, null=True)),
                ('rutaXml', models.CharField(blank=True, max_length=100, null=True)),
                ('rutaAd', models.CharField(blank=True, max_length=1000, null=True)),
                ('rutaXmlFirmado', models.CharField(blank=True, max_length=1000, null=True)),
                ('mensajeDian', models.CharField(blank=True, max_length=1000, null=True)),
                ('rutaXmlRta', models.CharField(blank=True, max_length=1000, null=True)),
                ('nombreArchivo', models.CharField(blank=True, max_length=1000, null=True)),
                ('estado', models.CharField(blank=True, max_length=100, null=True)),
                ('fechaEnvioDian', models.DateTimeField(blank=True, null=True)),
                ('reprocesarDian', models.CharField(blank=True, max_length=1, null=True)),
                ('estadoEnvioDyan', models.CharField(blank=True, max_length=1, null=True)),
                ('tipoFacturaDyan', models.CharField(blank=True, max_length=1, null=True)),
                ('rutaPdf', models.CharField(blank=True, max_length=100, null=True)),
                ('envioCorreo', models.CharField(blank=True, max_length=1, null=True)),
                ('desbloqueada', models.CharField(blank=True, max_length=1, null=True)),
                ('verLiquidacion', models.CharField(blank=True, max_length=1, null=True)),
                ('anticipos', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('numeroglosa', models.CharField(blank=True, max_length=20, null=True)),
                ('totalCantidadGlosada', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('totalValorGlosado', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('totalCantidadAceptada', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('totalValorAceptado', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('totalCantidadSoportado', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('totalValorSoportado', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('totalNotasCredito', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('totalNotasDebito', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('detalleAnulacion', models.CharField(blank=True, max_length=20, null=True)),
                ('fechaAnulacion', models.DateTimeField(blank=True, null=True)),
                ('observaciones', models.CharField(blank=True, max_length=100, null=True)),
                ('fechaRegistro', models.DateTimeField(blank=True, null=True)),
                ('estadoReg', models.CharField(default='A', editable=False, max_length=1)),
                ('convenio', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='Conv08', to='contratacion.Convenios')),
                ('motivoGlosa', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='Glosa01', to='cartera.MotivosGlosas')),
                ('tipoDoc', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='TiposDoc101', to='usuarios.TiposDocumento')),
                ('usuarioAnula', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='Plantas100', to='planta.Planta')),
                ('usuarioRegistro', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='Plantas101', to='planta.Planta')),
            ],
        ),
        migrations.CreateModel(
            name='FacturacionDetalle',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('documento', models.CharField(blank=True, max_length=30, null=True)),
                ('consecAdmision', models.IntegerField(blank=True, null=True)),
                ('consecutivoFactura', models.IntegerField(blank=True, null=True)),
                ('fecha', models.DateTimeField(blank=True, null=True)),
                ('cantidad', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('valorUnitario', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('valorTotal', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('cirugia', models.CharField(blank=True, max_length=1, null=True)),
                ('fechaCrea', models.DateTimeField(blank=True, null=True)),
                ('fechaModifica', models.DateTimeField(blank=True, null=True)),
                ('observaciones', models.CharField(blank=True, max_length=200, null=True)),
                ('numeroglosa', models.CharField(blank=True, max_length=20, null=True)),
                ('cantidadGlosada', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('valorGlosado', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('cantidadAceptada', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('valorAceptado', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('cantidadSoportado', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('valorSoportado', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('fechaNotaCredito', models.DateTimeField(blank=True, null=True)),
                ('numeroNotaCredito', models.CharField(blank=True, max_length=20, null=True)),
                ('valorNotaCredito', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('observacionNotaCredito', models.CharField(blank=True, max_length=200, null=True)),
                ('fechaOtraNotaCredito', models.DateTimeField(blank=True, null=True)),
                ('numeroOtraNotaCredito', models.CharField(blank=True, max_length=20, null=True)),
                ('valorOtraNotaCredito', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('observacionOtraNotaCredito', models.CharField(blank=True, max_length=200, null=True)),
                ('fechaRegistro', models.DateTimeField(blank=True, null=True)),
                ('estadoRegistro', models.CharField(blank=True, max_length=1, null=True)),
                ('codigoCups', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='TablaCups121', to='clinico.Examenes')),
                ('cums', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='Cums101', to='rips.RipsCums')),
                ('facturacion', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='Fact01', to='facturacion.Facturacion')),
                ('motivoGlosa', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='Motiv03', to='cartera.MotivosGlosas')),
                ('tipoDoc', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='TablaTiposDoc101', to='usuarios.TiposDocumento')),
                ('usuarioCrea', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='Planta105', to='planta.Planta')),
                ('usuarioModifica', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='Planta106', to='planta.Planta')),
                ('usuarioRegistro', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='Planta107', to='planta.Planta')),
            ],
        ),
        migrations.CreateModel(
            name='FormasLiquidacion',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fechaRegistro', models.DateTimeField(blank=True, null=True)),
                ('estadoReg', models.CharField(default='A', editable=False, max_length=1)),
                ('usuarioRegistro', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='planta.Planta')),
            ],
        ),
        migrations.CreateModel(
            name='Liquidacion',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('documento', models.CharField(blank=True, max_length=30, null=True)),
                ('consecAdmision', models.IntegerField(blank=True, null=True)),
                ('fecha', models.DateTimeField(blank=True, null=True)),
                ('totalCopagos', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('totalCuotaModeradora', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('totalProcedimientos', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('totalSuministros', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('totalLiquidacion', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('valorApagar', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('anulado', models.CharField(blank=True, max_length=1, null=True)),
                ('fechaCorte', models.DateTimeField(blank=True, null=True)),
                ('anticipos', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('detalleAnulacion', models.CharField(blank=True, max_length=120, null=True)),
                ('fechaAnulacion', models.DateTimeField(blank=True, null=True)),
                ('observaciones', models.CharField(blank=True, max_length=120, null=True)),
                ('fechaRegistro', models.DateTimeField(blank=True, null=True)),
                ('estadoRegistro', models.CharField(blank=True, max_length=1, null=True)),
                ('convenio', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='Convenio102', to='contratacion.Convenios')),
                ('tipoDoc', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='TiposDoc120', to='usuarios.TiposDocumento')),
                ('usuarioAnula', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='Planta108', to='planta.Planta')),
                ('usuarioRegistro', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='Planta109', to='planta.Planta')),
            ],
        ),
        migrations.CreateModel(
            name='LiquidacionDetalle',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('documento', models.CharField(blank=True, max_length=30, null=True)),
                ('consecAdmision', models.IntegerField(blank=True, null=True)),
                ('consecutivo', models.IntegerField(blank=True, null=True)),
                ('fecha', models.DateTimeField(blank=True, null=True)),
                ('cantidad', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('valorUnitario', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('valorTotal', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('cirugia', models.CharField(blank=True, max_length=1, null=True)),
                ('fechaCrea', models.DateTimeField(blank=True, null=True)),
                ('fechaModifica', models.DateTimeField(blank=True, null=True)),
                ('observaciones', models.CharField(blank=True, max_length=120, null=True)),
                ('fechaRegistro', models.DateTimeField(blank=True, null=True)),
                ('estadoRegistro', models.CharField(blank=True, max_length=1, null=True)),
                ('codigoCups', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='TablaCups101', to='clinico.Examenes')),
                ('cums', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='TablaCums101', to='rips.RipsCums')),
                ('tipoDoc', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='TiposDoc125', to='usuarios.TiposDocumento')),
                ('usuarioCrea', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='Planta120', to='planta.Planta')),
                ('usuarioModifica', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='Planat121', to='planta.Planta')),
                ('usuarioRegistro', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='Planta122', to='planta.Planta')),
            ],
        ),
        migrations.CreateModel(
            name='Refacturacion',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('documento', models.CharField(blank=True, max_length=30, null=True)),
                ('consecAdmision', models.IntegerField(blank=True, null=True)),
                ('fecha', models.DateTimeField(blank=True, null=True)),
                ('facturaInicial', models.CharField(blank=True, max_length=20, null=True)),
                ('facturaFinal', models.CharField(blank=True, max_length=20, null=True)),
                ('fechaRegistro', models.DateTimeField(blank=True, null=True)),
                ('estadoRegistro', models.CharField(blank=True, max_length=1, null=True)),
                ('tipoDoc', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='TiposDoc145', to='usuarios.TiposDocumento')),
                ('usuarioRegistro', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='Planta123', to='planta.Planta')),
            ],
        ),
    ]