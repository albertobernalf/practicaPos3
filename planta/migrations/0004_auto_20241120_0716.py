# Generated by Django 2.1.15 on 2024-11-20 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planta', '0003_auto_20240702_1521'),
    ]

    operations = [
        migrations.AlterField(
            model_name='planta',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='fotos'),
        ),
    ]