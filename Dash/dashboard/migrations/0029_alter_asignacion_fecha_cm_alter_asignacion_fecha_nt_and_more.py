# Generated by Django 4.1.7 on 2023-03-11 19:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0028_alter_asignacion_fecha_cm_alter_asignacion_fecha_nt_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asignacion',
            name='fecha_cm',
            field=models.DateField(blank=True, default=datetime.datetime(2023, 3, 11, 19, 18, 22, 718383, tzinfo=datetime.timezone.utc), null=True),
        ),
        migrations.AlterField(
            model_name='asignacion',
            name='fecha_nt',
            field=models.DateField(blank=True, default=datetime.datetime(2023, 3, 11, 19, 18, 22, 718383, tzinfo=datetime.timezone.utc), null=True),
        ),
        migrations.AlterField(
            model_name='asignacion',
            name='fecha_ta',
            field=models.DateField(blank=True, default=datetime.datetime(2023, 3, 11, 19, 18, 22, 718383, tzinfo=datetime.timezone.utc), null=True),
        ),
    ]