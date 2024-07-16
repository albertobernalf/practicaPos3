# Generated by Django 2.1.15 on 2024-07-11 12:04

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('usuarios', '0003_auto_20240710_1531'),
        ('clinico', '0012_ips'),
        ('sitios', '0011_sedesclinica_nit'),
    ]

    operations = [
        migrations.CreateModel(
            name='Empresas',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('documento', models.CharField(blank=True, max_length=30, null=True)),
                ('nombre', models.CharField(blank=True, max_length=50, null=True)),
                ('codigoEapb', models.CharField(blank=True, max_length=10, null=True)),
                ('direccion', models.CharField(blank=True, max_length=80, null=True)),
                ('telefono', models.CharField(blank=True, max_length=20, null=True)),
                ('representante', models.CharField(blank=True, max_length=80, null=True)),
                ('fosyga', models.CharField(default='N', editable=False, max_length=1)),
                ('particular', models.CharField(default='N', editable=False, max_length=1)),
                ('codigoPostal', models.CharField(blank=True, max_length=30, null=True)),
                ('responsableFiscal', models.CharField(blank=True, max_length=80, null=True)),
                ('identificadorDian', models.CharField(blank=True, max_length=80, null=True)),
                ('fechaRegistro', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('estadoReg', models.CharField(default='A', editable=False, max_length=1)),
                ('departamento', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='Depto01', to='sitios.Departamentos')),
                ('municipio', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='Muni01', to='sitios.Municipios')),
                ('regimen', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='clinico.Regimenes')),
                ('tipoDoc', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='usuarios.TiposDocumento')),
            ],
        ),
    ]
