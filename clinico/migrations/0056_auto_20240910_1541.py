# Generated by Django 2.1.15 on 2024-09-10 15:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clinico', '0055_auto_20240910_0950'),
    ]

    operations = [
        migrations.RenameField(
            model_name='signosvitales',
            old_name='glagowVerbal',
            new_name='glasgowVerbal',
        ),
    ]
