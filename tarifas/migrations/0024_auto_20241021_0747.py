# Generated by Django 2.1.15 on 2024-10-21 07:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clinico', '0092_examenes_uvraño'),
        ('tarifas', '0023_auto_20241021_0740'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='liquidacionhonorarios',
            name='grupoQx',
        ),
        migrations.AddField(
            model_name='liquidacionhonorarios',
            name='codigoCups',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='Cups117', to='clinico.Examenes'),
        ),
    ]