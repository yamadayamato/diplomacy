# Generated by Django 3.0.6 on 2020-05-23 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_namedcoastmapdata'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='winners',
            field=models.ManyToManyField(to='core.NationState'),
        ),
    ]
