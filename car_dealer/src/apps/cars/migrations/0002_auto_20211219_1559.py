# Generated by Django 3.0.6 on 2021-12-19 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='pollutant_class',
            field=models.CharField(choices=[('A+', 'A+'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E'), ('F', 'F'), ('G', 'G')], default='A+', max_length=20),
        ),
    ]
