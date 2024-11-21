# Generated by Django 2.1.15 on 2024-11-19 11:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rips', '0009_ripscums_principiosactivos'),
        ('admisiones', '0033_auto_20241015_1114'),
    ]

    operations = [
        migrations.AddField(
            model_name='ingresos',
            name='ripsDestinoUsuarioEgresoRecienNacido',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='ripssDestino12', to='rips.RipsDestinoEgreso'),
        ),
    ]