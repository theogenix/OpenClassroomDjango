# Generated by Django 3.2.18 on 2023-04-29 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0011_auto_20230429_1819'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='year',
            field=models.IntegerField(default=None),
        ),
    ]
