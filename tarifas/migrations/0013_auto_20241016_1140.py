# Generated by Django 2.1.15 on 2024-10-16 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tarifas', '0012_liquidacionhonorarios_descripcion'),
    ]

    operations = [
        migrations.AddField(
            model_name='liquidacionhonorarios',
            name='miaxUvr',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True),
        ),
        migrations.AddField(
            model_name='liquidacionhonorarios',
            name='minUvr',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True),
        ),
        migrations.AddField(
            model_name='liquidacionhonorarios',
            name='valorPropio',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True),
        ),
    ]
