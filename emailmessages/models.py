from django.db import models

# Create your models here.



class Provider(models.Model):
    smtp_server_address     =       models.CharField(max_length=128)
    tcp_port                =       models.IntegerField(default=995)
    
class Sender(models.Model):
    user                    =       models.CharField(max_length=128)
    password                =       models.CharField(max_length=128)
    provider                =       models.ForeignKey(Provider, on_delete=models.CASCADE)


class Reminder(models.Model):
    #32 Kb of text should be enough for anyone ;)
    text                    =       models.TextField(max_length=32768)
    final_date              =       models.DateField()
    
class EMailAccount(models.Model):
    email                   =       models.EmailField()
    description             =       models.CharField(max_length=200)
    
class EmailMessage(models.Model):
    
    #Signals when the mail sender must send this message. When
    #this date arrives the mailer is allowed to send this email. The
    #date is not exact!! 
    date           =       models.DateTimeField()
    
    
    
    #Who is going to receive this message?
    to                      =       models.ForeignKey( EMailAccount, on_delete=models.CASCADE)
    subject                 =       models.CharField(max_length=256)
    reminder                =       models.ForeignKey ( Reminder ,  on_delete=models.CASCADE)
    sender                  =       models.ForeignKey ( Sender, on_delete=models.CASCADE)
    
    
    