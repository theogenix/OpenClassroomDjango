from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Band(models.Model):
    class Genre(models.TextChoices):
        HIP_HOP='HH'
        SYNTH_POP='SP'
        ALTERNATIVE_ROCK='AR'

    name=models.fields.CharField(max_length=100)
    genre=models.fields.CharField(choices=Genre.choices,max_length=5,default='HH')
    biography=models.fields.CharField(max_length=1000,default='')
    year_formed=models.fields.IntegerField(
        validators=[MinValueValidator(1900),MaxValueValidator(2021)],default=2000
    )
    active=models.fields.BooleanField(default=True)
    official_homepage=models.fields.URLField(null=True,blank=True)

class Listing(models.Model):
    class Type(models.TextChoices):
        disques='Records'
        vetements='Clothing'
        affiches='Posters'
        divers='Miscellaneous'
    name=models.fields.CharField(max_length=100)
    description=models.fields.CharField(max_length=1000)
    sold=models.fields.BooleanField(default=True)
    year=models.fields.IntegerField(default=2000)
    type=models.fields.CharField(choices=Type.choices,max_length=20,default='Records')