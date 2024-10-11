# Generated by Django 5.0.4 on 2024-04-24 13:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('existences', '0002_alter_domaine_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='commentaires',
            name='notation',
        ),
        migrations.AlterField(
            model_name='artisan',
            name='notation',
            field=models.IntegerField(),
        ),
        migrations.AddField(
            model_name='commentaires',
            name='demande',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='existences.demande'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Notation',
        ),
    ]
