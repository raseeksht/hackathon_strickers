# Generated by Django 4.1.7 on 2023-09-17 01:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alert', '0003_rename_orgtype_orguser'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='status',
            field=models.CharField(default='', max_length=100),
        ),
    ]
