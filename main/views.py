from django.shortcuts import render
from . import models


def index(request):
    return render(request, 'front/index.html')

def about(request):
    return render(request, 'front/about.html')

def contact(request):
    return render(request, 'front/contact.html')

def pricing(request):
    return render(request, 'front/pricing.html')

def services(request):
    return render(request, 'front/services.html')

def teashop(request):
    return render(request, 'front/teashop.html')

def testimonies(request):
    return render(request, 'front/testimonies.html')