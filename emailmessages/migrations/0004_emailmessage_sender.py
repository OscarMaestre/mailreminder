# Generated by Django 2.1.1 on 2018-09-08 21:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('emailmessages', '0003_auto_20180908_2022'),
    ]

    operations = [
        migrations.AddField(
            model_name='emailmessage',
            name='sender',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='emailmessages.Sender'),
            preserve_default=False,
        ),
    ]
