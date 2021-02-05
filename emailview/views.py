from django.shortcuts import render

# Create your views here.
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from rest_framework.decorators import api_view
from rest_framework.response import Response



@api_view(['GET'])
def emailsendlogic(request):
    email = 'pooj98.pp@gmail.com'
    password = 'poojasri'
    send_to_email = request.GET.get('email')
    print (send_to_email)
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.ehlo()
    server.login(email,password)
    subject='From pooja'
    msg = MIMEMultipart()
    msg['From'] = email
    msg['To'] = send_to_email
    msg['Subject'] = subject
    body='helooo'

    msg.attach(MIMEText(body,'plain'))
    text = msg.as_string() 
    server.sendmail(email, send_to_email, text)
    server.close()
    return Response("sucess")