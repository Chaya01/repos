# Generated by Django 4.1.7 on 2023-03-11 19:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0026_alter_asignacion_fecha_cm_alter_asignacion_fecha_nt_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asignacion',
            name='fecha_cm',
            field=models.DateField(blank=True, default=datetime.datetime(2023, 3, 11, 19, 15, 18, 839807, tzinfo=datetime.timezone.utc), null=True),
        ),
        migrations.AlterField(
            model_name='asignacion',
            name='fecha_nt',
            field=models.DateField(blank=True, default=datetime.datetime(2023, 3, 11, 19, 15, 18, 839807, tzinfo=datetime.timezone.utc), null=True),
        ),
        migrations.AlterField(
            model_name='asignacion',
            name='fecha_sma',
            field=models.DateField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='asignacion',
            name='fecha_ta',
            field=models.DateField(blank=True, default=datetime.datetime(2023, 3, 11, 19, 15, 18, 839807, tzinfo=datetime.timezone.utc), null=True),
        ),
    ]
