# Generated by Django 2.1.15 on 2024-09-27 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinico', '0081_auto_20240925_0755'),
    ]

    operations = [
        migrations.AddField(
            model_name='historiaexamenes',
            name='mipres',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='examenes',
            name='codigoCups',
            field=models.CharField(blank=True, max_length=6),
        ),
    ]