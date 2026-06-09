from django.shortcuts import render
from .forms import*

# Create your views here.
def home(request):
    return render(request,'base.html')

def registro(request):
    data={
        "formulario":formularioregistro()
    }
    return render(request,'pages/registro.html', data)