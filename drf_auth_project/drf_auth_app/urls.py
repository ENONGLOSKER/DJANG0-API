from django.urls import path
from .views import register, login_view, logout_view, list_user, home,login_page

urlpatterns = [
    path('login_page/', login_page, name='login_page'),
    path('', home, name='home'),
    path('user/', list_user, name='list_user'),
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
]
