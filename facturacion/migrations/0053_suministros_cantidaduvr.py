# Generated by Django 2.1.15 on 2024-10-21 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facturacion', '0052_remove_conceptos_tipocups'),
    ]

    operations = [
        migrations.AddField(
            model_name='suministros',
            name='cantidadUvr',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
