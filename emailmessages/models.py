from django.db import models

# Create your models here.



class Provider(models.Model):
    smtp_server_address     =       models.CharField(max_length=128)
    tcp_port                =       models.IntegerField(default=995)
class Sender(models.Model):
    user                    =       models.CharField(max_length=128)
    password                =       models.CharField(max_length=128)
    provider                =       models.ForeignKey(Provider)


class Reminder(models.Model):
    #32 Kb of text should be enough for anyone ;)
    text                    =       models.TextField(max_length=32768)
    final_date              =       models.DateField()
    
    
class EmailMessage(models.Model):
    
    #Signals when the mail sender must send this message. When
    #this date arrive the mailer is allowed to send this email. The
    #date is not exact!! 
    date           =       models.DateTimeField()
    
    
    
    #Who is going to receive this message?
    to                      =       models.CharField(max_length=128)
    subject                 =       models.CharField(max_length=256)
    reminder                =       models.ForeignKey ( Reminder )
    
    
    