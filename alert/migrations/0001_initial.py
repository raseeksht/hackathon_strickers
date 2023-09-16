# Generated by Django 4.1.7 on 2023-09-16 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Laptop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('processor', models.CharField(max_length=200)),
                ('ram', models.CharField(max_length=200)),
                ('storageType', models.CharField(choices=[('SSD', 'SSD'), ('HDD', 'HDD')], max_length=200)),
                ('storageCapacity', models.CharField(max_length=200)),
                ('display', models.CharField(max_length=200)),
                ('graphics', models.CharField(max_length=200)),
                ('battery', models.CharField(max_length=200)),
                ('ssdExpansion', models.CharField(choices=[('available', True), ('not available', False)], default=True, max_length=200)),
                ('link', models.CharField(default='#', max_length=500)),
                ('price', models.CharField(default='N/A', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(default='', max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
    ]
