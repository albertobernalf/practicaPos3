# Generated by Django 2.1.15 on 2024-10-02 10:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admisiones', '0028_auto_20241001_1507'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ingresos',
            name='ripsDestinoUsuarioEgresoRecienNacido',
        ),
    ]
