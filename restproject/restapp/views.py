from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from django.core import serializers
from django.conf import settings
import json


# Create your views here.

@api_view(["POST"])
def Question(qstring):
    try:
        input = qstring.data['data']
        #initialize resp so that it is never null
        resp = input.lower();
        input = input.lower();
        #single test case
        if(input == "who is the best?"):
            resp = "sean is the best"
        elif("broke" in input):
            resp = "Have you tried turning it off and on again?"
        elif(input in {"who is this?", "who are you?", "are you real?"}):
            resp = "I am the UWIT chatbot!"
        elif(input == "what is the helpdesk number?"):
            resp = "The phone number for the Help Desk is: 307-766-4357"
        elif(input == "powder river"):
            resp = "Let 'R Buck!"
        elif(input == "where is the knowledge base?"):
            resp = "Knowledge Base is here: https://uwyo.teamdynamix.com/TDClient/KB/"
        elif(input in {"hello", "hi", "sup","yo", "hey", ""}):
            resp = "Hello! How can I help you today?"
        elif("password reset" in input or "reset my password" in input or "password" in input):
            resp = "To reset your password, go here: http://www.uwyo.edu/infotech/passreset/"
        elif(input in {"how do i get email on my phone?"} or "phone" in input):
            resp = "To get email on your phone, check out this article: http://www.uwyo.edu/infotech/services/email/365.asp"
        else:
            resp = "Sorry, I'm not sure how to answer that. Please check out the UWIT website to speak to a representative https://www.uwyo.edu/infotech/"

        return JsonResponse(resp, safe=False)

    except ValueError as e:
        return Response(e.args[0],status.HTTP_400_BAD_REQUEST)
