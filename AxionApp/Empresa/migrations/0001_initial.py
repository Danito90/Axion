# Generated by Django 3.1.2 on 2021-08-27 19:36

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('razonSocial', models.CharField(max_length=50, unique=True)),
                ('cuit', models.CharField(blank=True, max_length=11)),
                ('user', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Empresas',
                'ordering': ['razonSocial'],
            },
        ),
    ]
