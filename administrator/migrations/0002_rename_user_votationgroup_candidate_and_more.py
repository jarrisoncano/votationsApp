# Generated by Django 4.1.3 on 2022-11-03 01:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('administrator', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User_VotationGroup',
            new_name='Candidate',
        ),
        migrations.RenameField(
            model_name='vote',
            old_name='codUser_VotationGroup',
            new_name='codCandidate',
        ),
    ]
