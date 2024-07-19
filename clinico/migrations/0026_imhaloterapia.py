# Generated by Django 2.1.15 on 2024-07-18 16:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('planta', '0003_auto_20240702_1521'),
        ('usuarios', '0003_auto_20240710_1531'),
        ('clinico', '0025_oxigeno'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImHaloTerapia',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('consecAdmision', models.IntegerField(default=0)),
                ('folio', models.IntegerField(default=0)),
                ('fecha', models.DateTimeField()),
                ('salbutamol', models.CharField(blank=True, max_length=50)),
                ('ipratropio', models.CharField(blank=True, max_length=50)),
                ('beclometazona', models.CharField(blank=True, max_length=50)),
                ('berudual', models.CharField(blank=True, max_length=50)),
                ('fechaRegistro', models.DateTimeField(blank=True, null=True)),
                ('estadoReg', models.CharField(default='A', editable=False, max_length=1)),
                ('documento', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='DocumentoHistoria29', to='usuarios.Usuarios')),
                ('tipoDoc', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='usuarios.TiposDocumento')),
                ('usuarioRegistro', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='planta.Planta')),
            ],
        ),
    ]
