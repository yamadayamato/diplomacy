# Generated by Django 2.2.5 on 2019-11-30 19:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20191130_1801'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='supplycenter',
            name='nationality',
        ),
        migrations.DeleteModel(
            name='SupplyCenterState',
        ),
    ]
