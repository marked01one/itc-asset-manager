# Generated by Django 4.1.7 on 2023-03-30 22:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ManufacturerModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manufacturer_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='RegionModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='TransformerModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial_number', models.CharField(max_length=15, unique=True)),
                ('kva', models.FloatField()),
                ('date_created', models.DateField()),
                ('manufacturer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='backend.manufacturermodel')),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='backend.regionmodel')),
            ],
        ),
        migrations.CreateModel(
            name='FailureLogModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('failure_cause', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('date_failed', models.DateField(auto_now_add=True)),
                ('transformer', models.ForeignKey(on_delete=django.db.models.deletion.SET, to='backend.transformermodel')),
            ],
        ),
    ]
