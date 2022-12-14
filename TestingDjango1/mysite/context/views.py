from email.mime import application
from tkinter import N
from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render
from .models import *
from django.db.models import Q
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
# from rest_framework_simplejwt.tokens import RefreshToken
from django.http import HttpResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from rest_framework.views import APIView
from .models import *
from django.shortcuts import HttpResponse, redirect
from django import http
from django.views.decorators.csrf import csrf_exempt


# Create your views here.


# def sendSimpleEmail(request, emailto):
#     res = send_mail("Subject", "Description", "arnit@gmail.com", [emailto])
#     return HttpResponse('%s' % res)


@api_view(['POST'])
@csrf_exempt
def App(request):
    if request.method == 'POST':
        name = request.data.get('name')
        email = request.data.get('email')
        Name_Of_your_institution = request.data.get('Name_Of_your_institution')
        Your_qualifications = request.data.get('Your_qualifications')
        Linkedin_URL = request.data.get('Linkedin_URL')
        How_did_you_get_to_know_about_us = request.data.get('How_did_you_get_to_know_about_us')
        # Additional_File = request.POST.get('Additional_File')
        Which_track_did_you_want_to_pursue = request.data.get('Which_track_did_you_want_to_pursue')

        application_obj = Application(
            name=name,
            email=email,
            Name_Of_your_institution=Name_Of_your_institution,
            Your_qualifications=Your_qualifications,
            Linkedin_URL=Linkedin_URL,
            How_did_you_get_to_know_about_us=How_did_you_get_to_know_about_us,
            # Additional_File=Additional_File,
            Which_track_did_you_want_to_pursue=Which_track_did_you_want_to_pursue,
        )
        application_obj.save()
        print(application_obj)
        return HttpResponse("Applied")
