# Generated by Django 3.2.5 on 2021-07-15 23:31

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('cuit', models.CharField(max_length=11)),
            ],
        ),
        migrations.CreateModel(
            name='chPropio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('banco', models.CharField(max_length=50)),
                ('numCh', models.CharField(max_length=8)),
                ('fechaCarga', models.DateField(default=datetime.datetime(2021, 7, 15, 20, 31, 19, 192841))),
                ('fechaVto', models.DateField()),
                ('monto', models.DecimalField(decimal_places=2, max_digits=15)),
                ('pagado', models.BooleanField(default=False)),
                ('situacion', models.CharField(max_length=20)),
                ('proveedor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='chPropios.proveedor')),
            ],
        ),
    ]
