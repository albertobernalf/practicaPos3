# Generated by Django 2.1.15 on 2024-10-23 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinico', '0095_auto_20241023_0837'),
    ]

    operations = [
        migrations.AlterField(
            model_name='principiosactivos',
            name='nombre',
            field=models.CharField(max_length=300),
        ),
    ]
