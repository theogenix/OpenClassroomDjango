# Generated by Django 3.2.18 on 2023-04-29 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0008_alter_listing_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='year',
            field=models.IntegerField(default=2000),
        ),
    ]
