# Generated by Django 2.1.15 on 2024-08-29 11:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clinico', '0035_auto_20240829_1111'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='examenesradiologia',
            name='TiposExamen',
        ),
        migrations.RemoveField(
            model_name='examenesradiologia',
            name='concepto',
        ),
        migrations.RemoveField(
            model_name='examenesradiologia',
            name='tipoRadiologia',
        ),
        migrations.AlterField(
            model_name='historiaexamenes',
            name='examenesLaboratorio',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='exalab01', to='clinico.Examenes'),
        ),
        migrations.AlterField(
            model_name='historiaexamenes',
            name='examenesNoQx',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='clinico.Examenes'),
        ),
        migrations.AlterField(
            model_name='historiaexamenes',
            name='examenesRadiologia',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='exarad01', to='clinico.Examenes'),
        ),
        migrations.AlterField(
            model_name='historiaexamenes',
            name='examenesTerapias',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='exapro01', to='clinico.Examenes'),
        ),
        migrations.DeleteModel(
            name='ExamenesRadiologia',
        ),
    ]
