# Generated by Django 3.1.2 on 2021-08-08 20:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chPropios', '0010_alter_chpropio_fechacarga'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chpropio',
            name='banco',
            field=models.CharField(choices=[('CIUDAD', 'CIUDAD'), ('CREDICOOP', 'CREDICOOP'), ('HSBC', 'HSBC'), ('MACRO', 'MACRO'), ('NACION', 'NACION'), ('SANTANDER', 'SANTANDER'), ('SUPERVIELLE', 'SUPERVIELLE'), ('RIO', 'RIO')], max_length=50),
        ),
        migrations.AlterField(
            model_name='chpropio',
            name='fechaCarga',
            field=models.DateField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='chpropio',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='chpropio',
            name='numCh',
            field=models.CharField(max_length=8),
        ),
        migrations.AlterUniqueTogether(
            name='chpropio',
            unique_together={('banco', 'numCh')},
        ),
    ]
