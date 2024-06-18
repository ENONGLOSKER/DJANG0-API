# myapp/urls.py
from django.urls import path
from .views import LoginView, HomeView, LogoutView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('home/', HomeView.as_view(), name='home'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
