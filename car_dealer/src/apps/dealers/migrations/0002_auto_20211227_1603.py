# Generated by Django 3.0.6 on 2021-12-27 16:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('countries', '0001_initial'),
        ('dealers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dealer',
            name='city_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='countries.City', verbose_name='ID'),
        ),
    ]
