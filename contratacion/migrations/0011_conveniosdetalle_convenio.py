# Generated by Django 2.1.15 on 2024-10-16 09:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contratacion', '0010_conveniosdetalle_tipotarifa'),
    ]

    operations = [
        migrations.AddField(
            model_name='conveniosdetalle',
            name='convenio',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='contratacion.Convenios'),
        ),
    ]
