# Generated by Django 3.2.18 on 2023-04-29 21:41

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0020_listing_band'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='year',
            field=models.IntegerField(default=2000, validators=[django.core.validators.MinValueValidator(1900), django.core.validators.MaxValueValidator(2021)]),
        ),
    ]
