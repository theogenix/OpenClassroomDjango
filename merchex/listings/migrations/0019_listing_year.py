# Generated by Django 3.2.18 on 2023-04-29 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0018_auto_20230429_2219'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='year',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]