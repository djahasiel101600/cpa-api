from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from django.contrib.auth import authenticate
from rest_framework.views import APIView
import json

# Create your views here.
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

class RegisterUser(APIView):
    permission_classes = [AllowAny]
    
    def post(self, request):
        serializer = RegisterSerializer
        if serializer.is_valid():
            user = serializer.save()
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'token':token.key}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    
    
class LoginUser(APIView):
    permission_classes = [AllowAny]
    
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        
        user = authenticate(username=username, password=password)
        
        if user is not None:
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'token':token.key})
        
        return Response({'error':'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
    
class LogoutUser(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        user = Token.objects.get(key=request.auth)
        user.delete()
        return Response({'message':'user has already logged out'}, status=status.HTTP_201_CREATED)
        
class ProtectedView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        print("Protected View accessed")
        return Response({'message':"Authenticated"}, status=status.HTTP_200_OK)
    
class UserView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)