from django.shortcuts import render

# Create your views here.


# Create your views here.
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import requests
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])

def getemail(request):

      s="pooj98.pp@gmail.com"
      email= request.GET.get('s')
      var="http://127.0.0.1:8000/emailsendlogic?email=,s"
      
      response=requests.get(var)
      if(response.status_code==200):
            return  Response("sucess")
      else:
            return Response("failure")

      #print('email',email)
      return Response("no")