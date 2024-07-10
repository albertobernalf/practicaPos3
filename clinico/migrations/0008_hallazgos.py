# Generated by Django 2.1.15 on 2024-07-09 10:27

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('clinico', '0007_auto_20240708_1619'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hallazgos',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('miembrosSuperiores', models.CharField(choices=[('S', 'SI'), ('N', 'NO')], default='N', max_length=1)),
                ('miembrosInferiores', models.CharField(choices=[('S', 'SI'), ('N', 'NO')], default='N', max_length=1)),
                ('columna', models.CharField(choices=[('S', 'SI'), ('N', 'NO')], default='N', max_length=1)),
                ('ojos', models.CharField(choices=[('S', 'SI'), ('N', 'NO')], default='N', max_length=1)),
                ('nariz', models.CharField(choices=[('S', 'SI'), ('N', 'NO')], default='N', max_length=1)),
                ('oidos', models.CharField(choices=[('S', 'SI'), ('N', 'NO')], default='N', max_length=1)),
                ('cara', models.CharField(choices=[('S', 'SI'), ('N', 'NO')], default='N', max_length=1)),
                ('neurologicos', models.CharField(choices=[('S', 'SI'), ('N', 'NO')], default='N', max_length=1)),
                ('fxCraneo', models.CharField(choices=[('S', 'SI'), ('N', 'NO')], default='N', max_length=1)),
                ('torax', models.CharField(choices=[('S', 'SI'), ('N', 'NO')], default='N', max_length=1)),
                ('abdomen', models.CharField(choices=[('S', 'SI'), ('N', 'NO')], default='N', max_length=1)),
                ('exaMdGeneral', models.CharField(choices=[('S', 'SI'), ('N', 'NO')], default='N', max_length=1)),
                ('factorTvp', models.CharField(choices=[('S', 'SI'), ('N', 'NO')], default='N', max_length=1)),
                ('cuello', models.CharField(choices=[('S', 'SI'), ('N', 'NO')], default='N', max_length=1)),
                ('fechaRegistro', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('estadoReg', models.CharField(default='A', editable=False, max_length=1)),
            ],
        ),
    ]
