from django.shortcuts import render
from django.views.generic import ListView
from .models import Experiencia
# Create your views here.
#def ExpView(request):
#    return render(request,'experiencias.html')


class ExpView(ListView):
    model = Experiencia
    template_name = 'experiencias.html'
    ordering = ['-id']



