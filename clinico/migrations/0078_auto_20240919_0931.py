# Generated by Django 2.1.15 on 2024-09-19 09:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clinico', '0077_auto_20240919_0838'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historia',
            name='dependenciasRealizado',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='sitios.DependenciasTipo'),
        ),
    ]
