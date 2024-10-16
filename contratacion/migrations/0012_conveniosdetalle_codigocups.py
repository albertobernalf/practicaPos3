# Generated by Django 2.1.15 on 2024-10-16 10:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clinico', '0092_examenes_uvraño'),
        ('contratacion', '0011_conveniosdetalle_convenio'),
    ]

    operations = [
        migrations.AddField(
            model_name='conveniosdetalle',
            name='codigoCups',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='Cups110', to='clinico.Examenes'),
        ),
    ]
