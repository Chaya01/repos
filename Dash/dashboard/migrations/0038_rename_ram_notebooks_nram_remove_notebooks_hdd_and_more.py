# Generated by Django 4.1.7 on 2023-03-18 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0037_notebooks_hdd_notebooks_ram_notebooks_ssd'),
    ]

    operations = [
        migrations.RenameField(
            model_name='notebooks',
            old_name='ram',
            new_name='nram',
        ),
        migrations.RemoveField(
            model_name='notebooks',
            name='hdd',
        ),
        migrations.RemoveField(
            model_name='notebooks',
            name='ssd',
        ),
        migrations.AddField(
            model_name='notebooks',
            name='nhdd',
            field=models.IntegerField(default=1, help_text='Por favor marcar 0 si no tiene HDD', verbose_name='HDD'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='notebooks',
            name='nssd',
            field=models.IntegerField(default=1, help_text='Por favor marcar 0 si no tiene SSD', verbose_name='SSD'),
            preserve_default=False,
        ),
    ]
