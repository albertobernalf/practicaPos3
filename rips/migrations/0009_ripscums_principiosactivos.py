# Generated by Django 2.1.15 on 2024-10-23 14:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clinico', '0096_auto_20241023_1432'),
        ('rips', '0008_ripscums_viaadministracion'),
    ]

    operations = [
        migrations.AddField(
            model_name='ripscums',
            name='principiosActivos',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='ViasAdmon11', to='clinico.PrincipiosActivos'),
        ),
    ]