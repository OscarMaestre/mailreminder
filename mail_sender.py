#!/usr/bin/env python3

from emailmessages.Configurator import Configurator
configurador=Configurator(".")
configurador.activate("emailreminder.settings")
#from email_app.models import         

class EnviadorCorreo(object):
    @staticmethod
    def get_correos_pendientes_de_enviar():
        pass
        
    @staticmethod
    def enviar_correos_si_procede():
        
        lista_correos_pendientes=EnviadorCorreo.get_correos_pendientes_de_enviar()
        

    
    
if __name__ == '__main__':
    EnviadorCorreo.enviar_correos_si_procede()