# Generated by Django 4.1.7 on 2023-04-15 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0012_alter_usuarios_correo'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='usuarios',
            options={'ordering': ['nombre'], 'verbose_name': 'Trabajadores'},
        ),
        migrations.AlterField(
            model_name='usuarios',
            name='centro_de_costo',
            field=models.CharField(choices=[('Supervision Terreno JA', 'Supervision Terreno JA'), ('Supervision Terreno GC', 'Supervision Terreno GC'), ('Supervision Terreno Verano', 'Supervision Terreno Verano'), ('Supervision Terreno Invierno', 'Supervision Terreno Invierno'), ('Administracion', 'Administracion'), ('Parentales', 'Parentales'), ('Comex', 'Comex'), ('Planta Curimapu Los Tilos', 'Planta Curimapu Los Tilos'), ('Planta Semilla Humeda', 'Planta Semilla Humeda'), ('Planta Semilla Seca', 'Planta Semilla Seca'), ('Prevencion de Riesgo', 'Prevencion de Riesgo'), ('Operación Agricola', 'Operación Agricola'), ('Ventas', 'Ventas'), ('HomeFarm', 'HomeFarm'), ('Operaciones Agricolas', 'Operaciones Agricolas'), ('Laboratorio', 'Laboratorio'), ('Bodega', 'Bodega'), ('Operación Mantenimiento', 'Operación Mantenimiento'), ('Planta Maiz A', 'Planta Maiz A'), ('Planta Maiz B', 'Planta Maiz B'), ('SA', 'SA')], max_length=30, verbose_name='Centro de Costo'),
        ),
        migrations.AlterField(
            model_name='usuarios',
            name='correo',
            field=models.EmailField(blank=True, max_length=50, null=True),
        ),
    ]
