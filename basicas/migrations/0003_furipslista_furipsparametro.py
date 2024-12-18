# Generated by Django 2.1.15 on 2024-07-09 11:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('basicas', '0002_periodos'),
    ]

    operations = [
        migrations.CreateModel(
            name='FuripsLista',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('estadoReg', models.CharField(choices=[('S', 'S'), ('N', 'N')], default='A', editable=False, max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='FuripsParametro',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('estadoReg', models.CharField(choices=[('S', 'S'), ('N', 'N')], default='A', editable=False, max_length=1)),
                ('furipsLista', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='basicas.FuripsLista')),
            ],
        ),
    ]
