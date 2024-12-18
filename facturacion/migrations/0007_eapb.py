# Generated by Django 2.1.15 on 2024-07-19 12:25

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0003_auto_20240710_1531'),
        ('facturacion', '0006_conveniospaciente_conveniospacienteingresos'),
    ]

    operations = [
        migrations.CreateModel(
            name='Eapb',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('codigoEapb', models.CharField(blank=True, max_length=8, null=True)),
                ('nombre', models.CharField(max_length=30)),
                ('documento', models.CharField(blank=True, max_length=30, null=True)),
                ('direccion', models.CharField(blank=True, max_length=150, null=True)),
                ('telefono', models.CharField(blank=True, max_length=30, null=True)),
                ('codigoRips', models.CharField(blank=True, max_length=8, null=True)),
                ('fechaRegistro', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('estadoReg', models.CharField(default='A', editable=False, max_length=1)),
                ('tipoDoc', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='usuarios.TiposDocumento')),
            ],
        ),
    ]
