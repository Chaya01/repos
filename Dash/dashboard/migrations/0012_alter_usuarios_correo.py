# Generated by Django 4.1.7 on 2023-04-06 01:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0011_alter_usuarios_nombre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuarios',
            name='correo',
            field=models.EmailField(max_length=50, null=True),
        ),
    ]
