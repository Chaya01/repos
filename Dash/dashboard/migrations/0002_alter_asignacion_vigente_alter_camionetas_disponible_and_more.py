# Generated by Django 4.1.7 on 2023-03-23 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asignacion',
            name='vigente',
            field=models.BooleanField(help_text='marcar si es la asignacion actual del usuario.'),
        ),
        migrations.AlterField(
            model_name='camionetas',
            name='disponible',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='notebooks',
            name='estado_notebook',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='smartphones',
            name='estado_telefono',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='tablets',
            name='estado_tablet',
            field=models.BooleanField(),
        ),
    ]
