# Generated by Django 2.1.15 on 2024-09-12 08:57

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('planta', '0003_auto_20240702_1521'),
        ('usuarios', '0004_auto_20240822_0828'),
    ]

    operations = [
        migrations.CreateModel(
            name='MotivosGlosas',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('codigo', models.CharField(max_length=10)),
                ('nombre', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Pagos',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=30)),
                ('fecha', models.DateTimeField(blank=True, null=True)),
                ('consec', models.IntegerField()),
                ('valor', models.DecimalField(decimal_places=2, max_digits=20)),
                ('descripcion', models.CharField(max_length=200)),
                ('fechaRegistro', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('estadoReg', models.CharField(default='A', editable=False, max_length=1)),
                ('documento', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='Documento77', to='usuarios.Usuarios')),
                ('tipoDoc', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='usuarios.TiposDocumento')),
            ],
        ),
        migrations.CreateModel(
            name='Radicaciones',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fecha', models.DateTimeField(blank=True, null=True)),
                ('remision', models.CharField(max_length=20)),
                ('radicacion', models.CharField(max_length=20)),
                ('fechaRegistro', models.DateTimeField(blank=True, null=True)),
                ('estadoReg', models.CharField(default='A', editable=False, max_length=1)),
                ('usuarioRegistro', models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.PROTECT, to='planta.Planta')),
            ],
        ),
        migrations.CreateModel(
            name='Remisiones',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fecha', models.DateTimeField(blank=True, null=True)),
                ('remision', models.CharField(max_length=20)),
                ('fechaRegistro', models.DateTimeField(blank=True, null=True)),
                ('estadoReg', models.CharField(default='A', editable=False, max_length=1)),
                ('usuarioRegistro', models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.PROTECT, to='planta.Planta')),
            ],
        ),
        migrations.CreateModel(
            name='TiposGlosas',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='TiposPagos',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='pagos',
            name='tipoPago',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='cartera.TiposPagos'),
        ),
    ]
