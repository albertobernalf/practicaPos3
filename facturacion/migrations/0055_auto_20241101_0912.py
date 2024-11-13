# Generated by Django 2.1.15 on 2024-11-01 09:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('facturacion', '0054_auto_20241023_1529'),
    ]

    operations = [
        migrations.AlterField(
            model_name='facturacion',
            name='documento',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='DocumentoFac2', to='usuarios.Usuarios'),
        ),
        migrations.AlterField(
            model_name='liquidacion',
            name='documento',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='DocumentoFac3', to='usuarios.Usuarios'),
        ),
        migrations.AlterField(
            model_name='refacturacion',
            name='documento',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='DocumentoFac4', to='usuarios.Usuarios'),
        ),
    ]