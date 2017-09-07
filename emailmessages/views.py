from django.shortcuts import render

# Create your views here.


def index(peticion):
    return render (peticion, 'emailmessages/index.html', None)

def login(peticion):
    return render (peticion, 'emailmessages/login.html', None)