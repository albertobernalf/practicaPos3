# Generated by Django 2.1.15 on 2024-10-28 09:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('facturacion', '0054_auto_20241023_1529'),
        ('contratacion', '0021_remove_convenios_tipotarifa'),
    ]

    operations = [
        migrations.AddField(
            model_name='conveniosprocedimientos',
            name='concepto',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='Concepto21', to='facturacion.Conceptos'),
        ),
    ]
