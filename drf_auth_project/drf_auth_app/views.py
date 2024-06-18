from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth import login, logout
from .serializers import RegisterSerializer, LoginSerializer
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt


@api_view(['POST'])
def register(request):
    serializer = RegisterSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@csrf_exempt
def login_view(request):
    serializer = LoginSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.validated_data
        login(request, user)
        return Response({"message": "Logged in successfully"}, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def logout_view(request):
    logout(request)
    return Response({"message": "Logged out successfully"}, status=status.HTTP_200_OK)

@api_view(['GET'])
def list_user(request):
    users = User.objects.all()
    user_data = [{"username": user.username, "email": user.email, "password": user.password} for user in users]
    return Response(user_data, status=status.HTTP_200_OK)


def home(request):
    return render(request, 'index.html')

def login_page(request):
    return render(request, 'login.html')