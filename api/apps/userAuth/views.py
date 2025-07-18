from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from rest_framework.authtoken.models import Token

# Create your views here.
@csrf_exempt
def signin(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')
        
        userSignIn = authenticate(request, username=username, password=password)
        # print(Token.objects.get(User.objects.get(username=userSignIn.username)))
        if userSignIn is not None:
            login(request, userSignIn)
            return JsonResponse({"Token":"sdfsdfasd"})
        else:
            return JsonResponse({"error":"username not exists"})
    else:
        return JsonResponse({'error':'GET Request not Allowed'})
        