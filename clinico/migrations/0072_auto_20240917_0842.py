# Generated by Django 2.1.15 on 2024-09-17 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinico', '0071_examenes_grupoqx'),
    ]

    operations = [
        migrations.AddField(
            model_name='examenes',
            name='numeroUvr',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='examenes',
            name='citaControl',
            field=models.CharField(blank=True, max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='examenes',
            name='codigoRips',
            field=models.CharField(blank=True, max_length=6, null=True),
        ),
    ]