# Generated by Django 4.1.7 on 2023-04-06 01:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0010_alter_usuarios_centro_de_costo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuarios',
            name='nombre',
            field=models.CharField(max_length=30),
        ),
    ]
