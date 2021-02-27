from django.urls import path
from .views import ContactView

urlpatterns = [
    path('contactMe/', ContactView.as_view(), name='contacto'),
]
