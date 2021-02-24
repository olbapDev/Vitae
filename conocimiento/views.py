from django.shortcuts import render
from django.views.generic import ListView
from .models import Conocimiento
# Create your views here.
#def ExpView(request):
#    return render(request,'experiencias.html')


class ConocimientoView(ListView):
    model = Conocimiento
    template_name = 'conocimientos.html'
    ordering = ['-id']



