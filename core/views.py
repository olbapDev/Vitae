from django.shortcuts import render
from proyect.models import Project
# Create your views here.
def HomeView(request):
    projects= Project.objects.all()
    data={
        'proyectos': projects
    }
    return render(request,'home.html',data)
