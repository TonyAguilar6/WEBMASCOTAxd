# Generated by Django 2.0.6 on 2021-09-17 02:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='client',
            fields=[
                ('pk_client', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('tel', models.CharField(max_length=8)),
                ('direction', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'client',
                'verbose_name_plural': 'client',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='date',
            fields=[
                ('pk_date', models.AutoField(primary_key=True, serialize=False)),
                ('day', models.CharField(max_length=8)),
                ('hour', models.CharField(max_length=5)),
                ('fk_client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webmascota.client')),
            ],
            options={
                'verbose_name': 'date',
                'verbose_name_plural': 'date',
                'ordering': ['day'],
            },
        ),
        migrations.CreateModel(
            name='mascota',
            fields=[
                ('pk_mascota', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('type', models.CharField(max_length=50)),
                ('color', models.CharField(max_length=8)),
                ('age', models.CharField(max_length=2)),
                ('state', models.CharField(max_length=9)),
            ],
            options={
                'verbose_name': 'mascota',
                'verbose_name_plural': 'mascota',
                'ordering': ['name'],
            },
        ),
        migrations.AddField(
            model_name='date',
            name='fk_mascota',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webmascota.mascota'),
        ),
    ]
