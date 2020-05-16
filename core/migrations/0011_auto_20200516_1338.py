# Generated by Django 3.0.6 on 2020-05-16 13:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_namedcoast_piece_starts_here'),
    ]

    operations = [
        migrations.AddField(
            model_name='piecestate',
            name='must_retreat',
            field=models.BooleanField(default=False, help_text='Signifies that the piece was dislodged in the previous turn and now must retreat.'),
        ),
        migrations.AlterField(
            model_name='piecestate',
            name='dislodged_by',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='piece_dislodged', to='core.PieceState'),
        ),
        migrations.AlterField(
            model_name='variant',
            name='starting_year',
            field=models.PositiveIntegerField(default=1901),
        ),
    ]
