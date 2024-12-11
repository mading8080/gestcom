# Generated by Django 5.1.3 on 2024-11-24 13:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_fournisseur', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='fournisseur',
            options={'ordering': ['nom']},
        ),
        migrations.RenameField(
            model_name='fournisseur',
            old_name='Adresse',
            new_name='adresse',
        ),
        migrations.RenameField(
            model_name='fournisseur',
            old_name='Date_Creation',
            new_name='date_creation',
        ),
        migrations.RenameField(
            model_name='fournisseur',
            old_name='Email',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='fournisseur',
            old_name='Fax',
            new_name='fax',
        ),
        migrations.RenameField(
            model_name='fournisseur',
            old_name='idFournisseur',
            new_name='idfournisseur',
        ),
        migrations.RenameField(
            model_name='fournisseur',
            old_name='Nom',
            new_name='nom',
        ),
        migrations.RenameField(
            model_name='fournisseur',
            old_name='Prenom',
            new_name='prenom',
        ),
        migrations.RenameField(
            model_name='fournisseur',
            old_name='Tel1',
            new_name='tel1',
        ),
        migrations.RenameField(
            model_name='fournisseur',
            old_name='Tel2',
            new_name='tel2',
        ),
        migrations.RenameField(
            model_name='fournisseur',
            old_name='Ville',
            new_name='ville',
        ),
    ]
