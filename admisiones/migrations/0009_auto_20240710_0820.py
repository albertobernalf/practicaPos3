# Generated by Django 2.1.15 on 2024-07-10 08:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('admisiones', '0008_auto_20240709_1605'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingresos',
            name='medicoActual',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='id7', to='clinico.Medicos'),
        ),
        migrations.AlterField(
            model_name='ingresos',
            name='medicoIngreso',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='id6', to='clinico.Medicos'),
        ),
        migrations.AlterField(
            model_name='ingresos',
            name='medicoSalida',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='id8', to='clinico.Medicos'),
        ),
    ]
