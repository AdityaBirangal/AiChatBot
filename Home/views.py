import sys,os
from django.conf import settings
from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import json
from django.http import JsonResponse
from .chatbot import getresponse
import re
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_exempt
from django.template import loader
import random

def Chatbot(request):
    if request.method == 'GET':
        return render(request,"HTML/Chatbot.html")
    else:
        return HttpResponse("<h1>Error 404</h1>")

def get_bot_response(request):
    if request.method == "GET":
        
        userText = request.GET['msg']
       
        words=re.split('\s+', userText)
        
           
        print("getresponse")
        return HttpResponse(str(getresponse(userText)))
            
            
    else:
        return HttpResponse("<h1>Error 404</h1>")



    
        
