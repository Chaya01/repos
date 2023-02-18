# Generated by Django 4.0.4 on 2022-06-03 21:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0013_alter_equipos_serie_alter_equipos_usuario_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historial',
            name='equipo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='dashboard.equipos'),
        ),
        migrations.AlterField(
            model_name='historial',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='dashboard.usuarios'),
        ),
    ]