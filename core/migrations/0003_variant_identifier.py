# Generated by Django 3.0.7 on 2020-07-18 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_nation_flag'),
    ]

    operations = [
        migrations.AddField(
            model_name='variant',
            name='identifier',
            field=models.CharField(default='standard', max_length=100),
            preserve_default=False,
        ),
    ]
