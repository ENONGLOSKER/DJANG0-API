# myapp/views.py
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken

class LogoutView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({"detail": "Logout successful"}, status=200)
        except Exception as e:
            return Response({"detail": str(e)}, status=400)

class LoginView(APIView):
    def get(self, request):
        return render(request, 'login.html')

class HomeView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        return render(request, 'home.html')
