
from django.urls import path
from .views import ConocimientoView

urlpatterns = [
    path('know/', ConocimientoView.as_view() , name="conocimiento"),
]
