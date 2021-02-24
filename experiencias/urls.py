
from django.urls import path
from .views import ExpView

urlpatterns = [
    path('exp/', ExpView.as_view() , name="experiencia"),
]
