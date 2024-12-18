# Generated by Django 2.1.15 on 2024-09-10 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinico', '0056_auto_20240910_1541'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signosvitales',
            name='apache',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='signosvitales',
            name='cuna',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='signosvitales',
            name='frecCardiaca',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='signosvitales',
            name='frecRespiratoria',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='signosvitales',
            name='glasgow',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='signosvitales',
            name='glasgowMotora',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='signosvitales',
            name='glasgowOcular',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='signosvitales',
            name='glasgowVerbal',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='signosvitales',
            name='glucometria',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='signosvitales',
            name='ic',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='signosvitales',
            name='pvc',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='signosvitales',
            name='saturacion',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='signosvitales',
            name='tensionADiastolica',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='signosvitales',
            name='tensionAMedia',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='signosvitales',
            name='tensionASistolica',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
