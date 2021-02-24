
from django.urls import path
from .views import InterView

urlpatterns = [
    path('intereses/', InterView.as_view() , name="interes"),
]
