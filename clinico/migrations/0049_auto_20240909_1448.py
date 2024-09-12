# Generated by Django 2.1.15 on 2024-09-09 14:48

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('clinico', '0048_auto_20240906_0748'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='incapacidades',
            name='folio',
        ),
        migrations.AlterField(
            model_name='incapacidades',
            name='desdeFecha',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='incapacidades',
            name='hastaFecha',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
