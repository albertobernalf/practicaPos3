# Generated by Django 2.1.15 on 2024-07-08 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitios', '0007_auto_20240708_0909'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dependencias',
            name='consec',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
