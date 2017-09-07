from django.contrib import admin

from emailmessages.models import Provider, Sender, EmailMessage
# Register your models here.


admin.site.register(EmailMessage)
admin.site.register(Provider)
admin.site.register(Sender)