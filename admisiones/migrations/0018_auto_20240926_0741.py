# Generated by Django 2.1.15 on 2024-09-26 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admisiones', '0017_auto_20240925_1430'),
    ]

    operations = [
        migrations.AddField(
            model_name='ingresos',
            name='DestinoUsuarioEgresoRecienNacido',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AddField(
            model_name='ingresos',
            name='edadGestacional',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AddField(
            model_name='ingresos',
            name='numConsultasCPrenatal',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AddField(
            model_name='ingresos',
            name='pesoRecienNacido',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AddField(
            model_name='ingresos',
            name='recienNacido',
            field=models.CharField(default='N', editable=False, max_length=1),
        ),
    ]