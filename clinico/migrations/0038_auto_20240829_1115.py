# Generated by Django 2.1.15 on 2024-08-29 11:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clinico', '0037_auto_20240829_1115'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='examenesnoqx',
            name='TiposExamen',
        ),
        migrations.RemoveField(
            model_name='examenesnoqx',
            name='concepto',
        ),
        migrations.DeleteModel(
            name='ExamenesNoQx',
        ),
    ]
