from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from listings.models import Band
from listings.models import Listing
from listings.forms import ContactUsForm
from django.core.mail import send_mail
from django.shortcuts import redirect
def band_list(request):
    bands = Band.objects.all()
    return render(request, 
                  'listings/band_list.html',
                  {'bands':bands})

def band_detail(request, id):
  band = Band.objects.get(id=id)
  return render(request,
          'listings/band_detail.html',
          {'band': band})

def about(request):
    return render(request,'listings/about.html')

def listings(request):
    listings=Listing.objects.all()
    return render(request,
                  'listings/listings.html',
                  {'listings':listings})

def listings_detail(request,id):
    listing=Listing.objects.get(id=id)
    return render(request,
                  'listings/listings_detail.html',
                  {'listing':listing})


def contactUs(request):
    print('la méthode de requête est : ',request.method)
    print('les données POST sont : ', request.POST)
    if request.method=='POST':
        form=ContactUsForm(request.POST)
        if form.is_valid():
            send_mail(
            subject=f'Message from {form.cleaned_data["name"] or "anonyme"} via MerchEx Contact Us form',
            message=form.cleaned_data['message'],
            from_email=form.cleaned_data['email'],
            recipient_list=['admin@merchex.xyz'],
        )
        return redirect('email-sent')
    else:
        form=ContactUsForm()

    return render(request,
                  'listings/contact.html',
                  {'form':form})

def emailSent(request):
    return render(request,
                  'listings/email_sent.html')

