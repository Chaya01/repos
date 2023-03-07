# Generated by Django 4.1.7 on 2023-03-07 02:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0016_alter_asignacion_num'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asignacion',
            name='num',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dashboard.num_telefono'),
        ),
        migrations.AlterField(
            model_name='num_telefono',
            name='numero_tel',
            field=models.CharField(blank=True, max_length=9, null=True),
        ),
    ]