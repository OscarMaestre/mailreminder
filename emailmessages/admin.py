from django.contrib import admin

from emailmessages.models import Message, Provider, Sender
# Register your models here.


admin.site.register(Message)
admin.site.register(Provider)
admin.site.register(Sender)