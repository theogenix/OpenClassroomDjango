# Generated by Django 3.2.18 on 2023-04-29 16:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0012_alter_listing_year'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listing',
            name='year',
        ),
    ]
