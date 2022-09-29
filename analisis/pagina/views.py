from django.shortcuts import render
from .forms import biseccionForm
from .models import *
# Create your views here.

def index(request):
    return render(request, 'index.html')

def biseccion(request, id):
    data=biseccion.objects.get(pk=id)

    form=biseccionForm()
    context={'form':form, 'data':data}
    return render(request, 'biseccion.html', context)