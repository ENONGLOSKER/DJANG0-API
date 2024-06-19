from django.shortcuts import render
from django.contrib.auth import authenticate, logout
from django.contrib.auth.models import User
# rest framework
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

# Create your views here.
@api_view()
@permission_classes([IsAuthenticated])
def list_user(request):
    users = User.objects.all()
    user_data = [
        {"username": user.username, 
         "email": user.email, 
         "password": user.password
        } 
        for user in users
    ]
    return Response(user_data, status=status.HTTP_200_OK)

@api_view(['POST'])
def user_register(request):
    username = request.data.get('username')
    password = request.data.get('password')
    email = request.data.get('email')

    if not username or not password:
        return Response({'error':'username dan password harus diisi!'}, status=status.HTTP_400_BAD_REQUEST)
    
    if User.objects.filter(username=username).exists():
        return Response({'error':'user sudah ada!'}, status=status.HTTP_400_BAD_REQUEST)
    
    user = User.objects.create_user(username=username, password=password, email=email),
    return Response({'massage':'user berhasil di tambahkan!'}, status=status.HTTP_201_CREATED)


@api_view(['POST'])
def user_login(request):
    username = request.data.get('username')
    password = request.data.get('password')

    if not username or not password:
        return Response({'error':'username dan password harus terisi'}, status=status.HTTP_400_BAD_REQUEST)
    
    user=authenticate(username=username, password=password)
    if user is not None:
        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh':str(refresh),
            'access':str(refresh.access_token)
        })
    else:
        return Response({'error': 'credential tidak benar!'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def user_logout(request):
    try:
        refresh_token = request.data["refresh"]
        token = RefreshToken(refresh_token)
        token.blacklist()
        return Response(status=status.HTTP_205_RESET_CONTENT)
    except Exception as e:
        return Response(status=status.HTTP_400_BAD_REQUEST)