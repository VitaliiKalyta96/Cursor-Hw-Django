# Generated by Django 3.0.6 on 2021-12-25 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0006_auto_20211225_1751'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fueltype',
            name='id',
        ),
        migrations.AddField(
            model_name='fueltype',
            name='fuel_id',
            field=models.IntegerField(default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]
