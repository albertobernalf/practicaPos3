# Generated by Django 2.1.15 on 2024-10-17 16:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('facturacion', '0049_auto_20241017_1208'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='facturaciondetalle',
            name='consecAdmision',
        ),
        migrations.RemoveField(
            model_name='facturaciondetalle',
            name='documento',
        ),
        migrations.RemoveField(
            model_name='facturaciondetalle',
            name='tipoDoc',
        ),
        migrations.RemoveField(
            model_name='liquidaciondetalle',
            name='consecAdmision',
        ),
        migrations.RemoveField(
            model_name='liquidaciondetalle',
            name='documento',
        ),
        migrations.RemoveField(
            model_name='liquidaciondetalle',
            name='tipoDoc',
        ),
        migrations.AddField(
            model_name='liquidaciondetalle',
            name='liquidacion',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='Liquid01', to='facturacion.Liquidacion'),
        ),
    ]