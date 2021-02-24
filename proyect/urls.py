
from django.urls import path
from .views import ProjectView

urlpatterns = [
    path('prox/', ProjectView.as_view() , name="proyecto"),
]
