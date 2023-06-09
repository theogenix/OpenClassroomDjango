# Generated by Django 3.2.18 on 2023-04-29 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0010_auto_20230429_1817'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='description',
            field=models.CharField(default='', max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='listing',
            name='sold',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='listing',
            name='type',
            field=models.CharField(choices=[('Records', 'Disques'), ('Clothing', 'Vetements'), ('Posters', 'Affiches'), ('Miscellaneous', 'Divers')], default='Records', max_length=20),
        ),
        migrations.AddField(
            model_name='listing',
            name='year',
            field=models.IntegerField(default=2000),
        ),
    ]
