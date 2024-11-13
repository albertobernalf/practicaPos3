# Generated by Django 2.1.15 on 2024-10-29 16:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('facturacion', '0054_auto_20241023_1529'),
        ('contratacion', '0023_auto_20241029_0715'),
    ]

    operations = [
        migrations.AddField(
            model_name='conveniossuministros',
            name='concepto',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='Concepto221', to='facturacion.Conceptos'),
        ),
    ]