# Generated by Django 3.0.6 on 2021-12-19 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NewsLetter',
            fields=[
                ('news_letter_id', models.IntegerField(primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=30)),
            ],
        ),
    ]
