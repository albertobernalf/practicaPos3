# Generated by Django 2.1.15 on 2024-10-30 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tarifas', '0039_auto_20241030_1055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='liquidaciontarifashonorarios',
            name='descripcion',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
