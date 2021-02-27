from django import forms
from .models import Contacto


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields =('name','correo','mensaje')
        widgets ={
            'name': forms.TextInput(attrs={'class': 'form-control','placeholder':'Tu hermoso nombre' }),
            'correo': forms.TextInput(attrs={'class': 'form-control'}),
            'mensaje': forms.Textarea(attrs={'class': 'form-control'}),
        }