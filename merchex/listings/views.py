from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from listings.models import Band
from listings.models import Listing
def hello(request):
    bands = Band.objects.all()
    return render(request, 
                  'listings/hello.html',
                  {'bands':bands})

def about(request):
    return render(request,'listings/about.html')

def listings(request):
    listing=Listing.objects.all()
    return render(request,
                  'listings/listings.html',
                  {'listing':listing})


def contactUs(request):
    return render(request,'listings/contact.html')