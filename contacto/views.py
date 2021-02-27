from django.shortcuts import render
from django.views.generic import CreateView
from .models import Contacto
from .forms import ContactForm
#from django.core.mail import send_mail



class ContactView(CreateView):
    model = Contacto
    form_class = ContactForm
    template_name = 'contacto.html'






# Create your views here.
# def ContactView(request):
#     if request.method == 'POST':
#         message_name = request.POST['message-name']
#         message_email = request.POST['message-email']
#         message = request.POST['message']
        
#         #sending an email
#         send_mail(
#             #este es el orden 
#             # asunto, mensajeTotal, email de quien lo envio, a quien va... se pueden colocar mas emails destinos agregando comas.
#             'message from: '+ message_name ,#subject
#             message,#message
#             message_email,#from email
#             ['pablo.garrido.cid@gmail.com'],#to email

#         )

#         return render(request, 'contacto.html',{'message_name':message_name})
#     else: 
#         return render(request, 'contacto.html',{})