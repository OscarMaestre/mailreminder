from django.shortcuts import render
from django.forms import ModelForm
from .models import EmailMessage
# Create your views here.



class EmailForm(ModelForm):
    class Meta:
        model = EmailMessage
        fields=["date", "to", "subject", "reminder", "sender"]
        
def index(peticion):
    return render (peticion, 'emailmessages/index.html', None)

def login(peticion):
    return render (peticion, 'emailmessages/login.html', None)

def create_reminder(peticion):
    if peticion.POST:
        process_petition (peticion)
    else:
        formulario_email = EmailForm()
        diccionario=dict()
        diccionario["formulario_email"]=formulario_email
        return render (peticion, 'emailmessages/create_reminder.html', diccionario)