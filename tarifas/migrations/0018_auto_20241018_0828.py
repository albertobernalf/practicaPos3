# Generated by Django 2.1.15 on 2024-10-18 08:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tarifas', '0017_auto_20241018_0816'),
    ]

    operations = [
        migrations.RenameField(
            model_name='liquidacionhonorariosiss',
            old_name='miaxUvr',
            new_name='maxUvr',
        ),
    ]