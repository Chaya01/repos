# Generated by Django 4.1.7 on 2023-03-18 18:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0040_alter_tablets_imei_tb'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='num_telefono',
            options={'verbose_name': 'Telefono'},
        ),
        migrations.AlterModelOptions(
            name='usuarios',
            options={'verbose_name': 'Trabajadores'},
        ),
    ]