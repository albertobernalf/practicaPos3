# Generated by Django 2.1.15 on 2024-08-30 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinico', '0042_auto_20240829_1523'),
    ]

    operations = [
        migrations.AddField(
            model_name='historiaexamenes',
            name='codigoCups',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
