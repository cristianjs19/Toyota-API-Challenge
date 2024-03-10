# Generated by Django 3.2 on 2024-03-07 03:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Characteristic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, default='', max_length=150)),
                ('description', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_name', models.CharField(default='', max_length=100)),
                ('subtitle', models.CharField(blank=True, default='', max_length=150)),
                ('description', models.TextField(blank=True, null=True)),
                ('type', models.IntegerField(choices=[(1, 'Autos'), (2, 'Pickups y Comerciales'), (3, 'SUVs y Crossovers')], default=1)),
                ('year', models.IntegerField(default=0)),
                ('price', models.IntegerField(default=0)),
                ('image', models.ImageField(blank=True, upload_to='images/')),
                ('active', models.BooleanField(default=True)),
                ('characteristics', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='vehicles.characteristic')),
            ],
        ),
    ]
