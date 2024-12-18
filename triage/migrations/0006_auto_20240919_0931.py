# Generated by Django 2.1.15 on 2024-09-19 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('triage', '0005_triage_consecadmision'),
    ]

    operations = [
        migrations.AlterField(
            model_name='triage',
            name='cinematicaTrauma',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='triage',
            name='escalaDolor',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='triage',
            name='estatura',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='triage',
            name='frecCardiaca',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='triage',
            name='frecRespiratoria',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='triage',
            name='glasgow',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='triage',
            name='glucometria',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='triage',
            name='peso',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='triage',
            name='saturacion',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='triage',
            name='taDiast',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='triage',
            name='taMedia',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='triage',
            name='taSist',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='triage',
            name='temperatura',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='triage',
            name='tipoIngreso',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='triage',
            name='tipoTrauma',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='triage',
            name='vistobno',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
