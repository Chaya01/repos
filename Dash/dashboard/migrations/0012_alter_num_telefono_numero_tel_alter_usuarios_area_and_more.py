# Generated by Django 4.0.4 on 2022-06-03 19:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0011_alter_usuarios_area_alter_usuarios_telefono'),
    ]

    operations = [
        migrations.AlterField(
            model_name='num_telefono',
            name='numero_tel',
            field=models.CharField(max_length=9, null=True),
        ),
        migrations.AlterField(
            model_name='usuarios',
            name='area',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='dashboard.departamentos'),
        ),
        migrations.AlterField(
            model_name='usuarios',
            name='telefono',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='dashboard.num_telefono'),
        ),
    ]