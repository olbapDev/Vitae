from django.shortcuts import render
from django.views.generic import ListView
from .models import Project
# Create your views here.
#def ExpView(request):
#    return render(request,'experiencias.html')


class ProjectView(ListView):
    model = Project
    template_name = 'proyectos.html'
    ordering = ['-id']

