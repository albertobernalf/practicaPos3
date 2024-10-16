# Generated by Django 2.1.15 on 2024-07-08 16:19

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('basicas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Periodos',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('año', models.IntegerField()),
                ('mes', models.IntegerField()),
                ('diaInicial', models.DateTimeField(default=django.utils.timezone.now)),
                ('diaFinal', models.DateTimeField(default=django.utils.timezone.now)),
                ('fechaRegistro', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('estadoReg', models.CharField(default='A', editable=False, max_length=1)),
            ],
        ),
    ]
