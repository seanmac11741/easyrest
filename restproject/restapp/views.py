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
        #single test case
        if(input == "who is the best?"):
            resp = "sean is the best"
        elif(input == "computer broke"):
            resp = "Have you tried turning it off and on again?"
        elif(input == "who is this?"):
            resp = "I am the UWIT chatbot!"
        elif(input == "what is the helpdesk number?"):
            resp = "The phone number for the Help Desk is: 307-766-4357"
        elif(input == "powder river"):
            resp = "Let 'R Buck!"
        elif(input == "where is the knowledge base?"):
            resp = "Knowledge Base is here: https://uwyo.teamdynamix.com/TDClient/KB/"
        elif(input in {"hello", "hi", "sup","yo", "hey", ""}):
            resp = "Hello! How can I help you today?"
        else:
            resp = "Sorry, I'm not sure how to answer that. Please check out the UWIT website to speak to a representative https://www.uwyo.edu/infotech/"

        return JsonResponse(resp, safe=False)

    except ValueError as e:
        return Response(e.args[0],status.HTTP_400_BAD_REQUEST)
