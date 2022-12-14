# Generated by Django 4.1.3 on 2022-11-01 14:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rol',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rol', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=500)),
                ('lastName', models.CharField(max_length=500)),
                ('password', models.CharField(max_length=500)),
                ('idRol', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administrator.rol')),
            ],
        ),
        migrations.CreateModel(
            name='User_VotationGroup',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('idUser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administrator.user')),
            ],
        ),
        migrations.CreateModel(
            name='VotationGroup',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=100)),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField()),
                ('date', models.DateField()),
                ('codUser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administrator.user')),
                ('codUser_VotationGroup', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administrator.user_votationgroup')),
            ],
        ),
        migrations.AddField(
            model_name='user_votationgroup',
            name='idVotationGroup',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administrator.votationgroup'),
        ),
    ]
