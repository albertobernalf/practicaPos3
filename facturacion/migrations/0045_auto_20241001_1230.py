# Generated by Django 2.1.15 on 2024-10-01 12:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('facturacion', '0044_auto_20241001_1218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='suministros',
            name='ripsTipoMedicamento',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='RipsTipo01', to='rips.RipsTipoMedicamento'),
        ),
    ]
