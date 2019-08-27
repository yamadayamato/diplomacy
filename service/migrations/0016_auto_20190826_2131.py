# Generated by Django 2.1.7 on 2019-08-26 21:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0015_auto_20190826_2112'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='move',
            name='type',
        ),
        migrations.AlterField(
            model_name='move',
            name='target_territory',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='target_commands', to='service.Territory'),
            preserve_default=False,
        ),
    ]
