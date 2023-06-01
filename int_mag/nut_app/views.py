from django.shortcuts import render
from nut_app.models import *


# Create your views here.

def home(request):
    data=Nut.objects.all()
    return render(request, 'nut_app/home.html',{'Nuts':data})