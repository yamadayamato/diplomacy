# Generated by Django 2.1.7 on 2019-05-06 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0010_auto_20190506_2109'),
    ]

    operations = [
        migrations.AddField(
            model_name='piece',
            name='must_disband',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='piece',
            name='must_retreat',
            field=models.BooleanField(default=False),
        ),
    ]