from django.shortcuts import render
from rest_framework import viewsets
from .serializers import UserSerializer
from .models import User
from django.contrib import messages
from django.core.paginator import Paginator
import json
from django.http import JsonResponse
from django.http import HttpResponse
from django.contrib.auth import authenticate
from rest_framework.renderers import JSONRenderer
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
import requests

# Create your views here.
class UserView(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

@csrf_exempt
def user(request):
    responses = {}
    responses['Access-Control-Allow-Origin'] = "*"
    responses['Access-Control-Request-Methods'] = "GET, PUT, POST, OPTIONS, DELETE"

    infos = request
    if request.method == "POST":
        email = request.POST.get('email')
        serializer = User(email=email)
        serializer.save()
        responses['message'] = True
        return JsonResponse(responses, status=201, safe=False)