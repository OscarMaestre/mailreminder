#!/usr/bin/env python3
#coding=utf-8


import os
import sys
import django

class Configurator(object):
    def __init__(self, ruta_proyecto):
        sys.path.append ( ruta_proyecto )
        
    def activate(self, paquete_settings):
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', paquete_settings)
        django.setup()