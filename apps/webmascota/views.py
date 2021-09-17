from django.shortcuts import render
from.models import *

# Create your views here.
def index(request):
    allmascota = mascota.objects.all()
    allclient = client.objects.all()
    alldate = date.objects.all()
    return render(request, 'index.html', {'allmascota':allmascota, 'allclient':allclient, 'alldate':alldate})
