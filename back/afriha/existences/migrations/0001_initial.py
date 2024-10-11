# Generated by Django 5.0.4 on 2024-04-22 18:49

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Domaine',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nom_domaine', models.CharField(max_length=255)),
                ('photo', models.BinaryField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Notation',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('notation', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('notification', models.CharField(max_length=255)),
                ('vue', models.BooleanField()),
                ('date_envoie', models.DateTimeField()),
            ],
            options={
                'ordering': ['date_envoie'],
            },
        ),
        migrations.CreateModel(
            name='Administrator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('administrator_id', models.CharField(max_length=10, unique=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='administrator_account', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Artisan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wilaya', models.CharField(max_length=255)),
                ('commune', models.CharField(max_length=255)),
                ('num_phone', models.IntegerField(unique=True)),
                ('domaine_expertise', models.CharField(max_length=255)),
                ('status', models.BooleanField(default=False)),
                ('diplome', models.TextField()),
                ('nb_interventions', models.IntegerField()),
                ('banni', models.BooleanField(default=False)),
                ('artisan_id', models.CharField(max_length=10, unique=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='artisan_account', to=settings.AUTH_USER_MODEL)),
                ('domaine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='existences.domaine')),
                ('notation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='existences.notation')),
            ],
        ),
        migrations.CreateModel(
            name='ArtisanWaiting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255)),
                ('prenom', models.CharField(max_length=255)),
                ('num_phone', models.IntegerField(unique=True)),
                ('wilaya', models.CharField(max_length=255)),
                ('commune', models.CharField(max_length=255)),
                ('photo', models.BinaryField(blank=True, null=True)),
                ('domaine_expertise', models.CharField(max_length=255)),
                ('diplome', models.TextField()),
                ('artisanWaiting_id', models.CharField(max_length=10, unique=True)),
                ('artisan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='existences.artisan')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='artisanWaiting_account', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wilaya', models.CharField(max_length=255)),
                ('commune', models.CharField(max_length=255)),
                ('adresse', models.CharField(max_length=255)),
                ('num_phone', models.IntegerField(unique=True)),
                ('client_id', models.CharField(max_length=10, unique=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='client_account', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Dialogue',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('artisan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='existences.artisan')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='existences.client')),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Message', models.TextField()),
                ('emiteur_recipteur', models.BooleanField()),
                ('dialogue', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='existences.dialogue')),
            ],
        ),
        migrations.CreateModel(
            name='Commentaires',
            fields=[
                ('creer', models.DateTimeField(auto_now_add=True)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('commentaire', models.TextField()),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='existences.client')),
                ('notation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='existences.notation')),
            ],
        ),
        migrations.CreateModel(
            name='Prestation',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nom_prestation', models.CharField(max_length=255)),
                ('prix_approximatif', models.FloatField()),
                ('duree_de_realisation', models.TimeField()),
                ('materiel_necessaire', models.TextField()),
                ('domaine_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='existences.domaine')),
            ],
        ),
        migrations.CreateModel(
            name='Demande',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('type', models.CharField(default='simple', max_length=255)),
                ('localisation', models.CharField(max_length=255)),
                ('date', models.DateField()),
                ('heure_debut', models.TimeField(null=True)),
                ('heure_fin', models.TimeField(null=True)),
                ('description', models.TextField(null=True)),
                ('Tarif', models.FloatField()),
                ('highlighted', models.TextField()),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='demandes', to=settings.AUTH_USER_MODEL)),
                ('domaine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='existences.domaine')),
                ('prestation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='existences.prestation')),
            ],
            options={
                'ordering': ['created_at'],
            },
        ),
        migrations.CreateModel(
            name='RendezVous',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateField()),
                ('Confirme', models.BooleanField(default=False)),
                ('artisan', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='existences.artisan')),
                ('demande', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='existences.demande')),
            ],
        ),
    ]
