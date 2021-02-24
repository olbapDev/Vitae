from django.shortcuts import render
from django.views.generic import ListView
from .models import Interes
# Create your views here.
#def ExpView(request):
#    return render(request,'experiencias.html')


class InterView(ListView):
    model = Interes
    template_name = 'intereses.html'
    ordering = ['id']



