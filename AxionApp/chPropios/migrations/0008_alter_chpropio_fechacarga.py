# Generated by Django 3.2.5 on 2021-08-02 22:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chPropios', '0007_alter_chpropio_fechacarga'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chpropio',
            name='fechaCarga',
            field=models.DateField(default=datetime.datetime(2021, 8, 2, 19, 19, 4, 803940)),
        ),
    ]
