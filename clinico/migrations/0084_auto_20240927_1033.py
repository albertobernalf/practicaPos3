# Generated by Django 2.1.15 on 2024-09-27 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinico', '0083_auto_20240927_1028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='examenes',
            name='codigoCups',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]