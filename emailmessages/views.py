from django.shortcuts import render

# Create your views here.


def index(peticion):
    return render (peticion, 'emailmessages/index.html', None)