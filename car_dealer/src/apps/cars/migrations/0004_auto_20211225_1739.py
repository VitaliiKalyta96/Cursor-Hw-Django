# Generated by Django 3.0.6 on 2021-12-25 17:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0003_auto_20211225_1731'),
    ]

    operations = [
        migrations.RenameField(
            model_name='car',
            old_name='fuel_type',
            new_name='fuel_type_id',
        ),
        migrations.RenameField(
            model_name='fueltype',
            old_name='fuel_type_car',
            new_name='fuel_type_car_id',
        ),
        migrations.RenameField(
            model_name='fueltype',
            old_name='fuel_type',
            new_name='fuel_type_id',
        ),
    ]
