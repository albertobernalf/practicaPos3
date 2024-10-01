# Generated by Django 2.1.15 on 2024-09-30 09:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tarifas', '0004_auto_20240930_0905'),
        ('facturacion', '0039_auto_20240930_0902'),
    ]

    operations = [
        migrations.AlterField(
            model_name='liquidacionderechos',
            name='tipoSala',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='tarifas.TiposSalas'),
        ),
        migrations.AlterField(
            model_name='liquidacionderechosiss',
            name='tipoSala',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='tarifas.TiposSalas'),
        ),
        migrations.DeleteModel(
            name='TiposSalas',
        ),
    ]
