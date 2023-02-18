# Generated by Django 4.0.4 on 2022-06-03 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0008_alter_usuarios_area_alter_usuarios_telefono'),
    ]

    operations = [
        migrations.AlterField(
            model_name='departamentos',
            name='area',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='usuarios',
            name='area',
            field=models.ForeignKey(on_delete=models.SET('null'), to='dashboard.departamentos'),
        ),
        migrations.AlterField(
            model_name='usuarios',
            name='telefono',
            field=models.ForeignKey(on_delete=models.SET('null'), to='dashboard.num_telefono'),
        ),
    ]