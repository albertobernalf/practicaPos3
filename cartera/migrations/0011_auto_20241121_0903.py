# Generated by Django 2.1.15 on 2024-11-21 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cartera', '0010_auto_20241121_0806'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pagos',
            name='totalAplicado',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=20, null=True),
        ),
    ]
