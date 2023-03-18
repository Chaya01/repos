# Generated by Django 4.1.7 on 2023-03-18 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0036_alter_camionetas_modalidad_alter_departamentos_area_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='notebooks',
            name='hdd',
            field=models.IntegerField(default=1, verbose_name='HDD'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='notebooks',
            name='ram',
            field=models.IntegerField(default=1, verbose_name='Memoria Ram'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='notebooks',
            name='ssd',
            field=models.IntegerField(default=1, verbose_name='SSD'),
            preserve_default=False,
        ),
    ]
