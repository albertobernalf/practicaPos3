# Generated by Django 2.1.15 on 2024-09-30 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admisiones', '0024_remove_ingresos_ripsdestinousuarioegresoreciennacido'),
    ]

    operations = [
        migrations.AddField(
            model_name='ingresos',
            name='ripsDestinoUsuarioEgresoRecienNacido',
            field=models.CharField(blank=True, default='', max_length=10, null=True),
        ),
    ]