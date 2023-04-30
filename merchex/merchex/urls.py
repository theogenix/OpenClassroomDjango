"""merchex URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from listings import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bands/',views.band_list,name='band-list'),
    path('bands/<int:id>/',views.band_detail, name='band-detail'),
    path('about-us/',views.about,name='about-us'),
    path('listings/', views.listings,name='listing-list'),
    path('listings/<int:id>/',views.listings_detail,name='listing-detail'),
    path('contact-us/',views.contactUs),
    path('contact-us/',views.contactUs,name='contact'),
    path('email-sent/',views.emailSent,name='email-sent'),
    path('bands/add/',views.band_create, name='band-create'),
    path('listings/add/', views.listing_create,name='listing-create'),
    path('bands/<int:id>/update/',views.band_update,name='band-update'),
    path('listings/<int:id>/update/', views.listing_update, name='listing-update'),
    path('bands/<int:id>/delete/',views.band_delete,name='band-delete'),
    path('listings/<int:id>',views.listing_delete,name='listing-delete'),

]   