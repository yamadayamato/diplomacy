# Generated by Django 2.1.7 on 2019-09-01 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0022_build_piece_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='supplycenter',
            name='controlled_by',
        ),
        migrations.AddField(
            model_name='supplycenter',
            name='initial_piece_type',
            field=models.CharField(choices=[('army', 'Army'), ('fleet', 'Fleet')], default=1, max_length=50),
            preserve_default=False,
        ),
    ]