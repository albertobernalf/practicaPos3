# Generated by Django 2.1.15 on 2024-10-15 12:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tarifas', '0004_auto_20240930_0905'),
    ]

    operations = [
        migrations.AddField(
            model_name='tarifas',
            name='uvrAño',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='Uvr101', to='tarifas.Uvr'),
        ),
    ]
