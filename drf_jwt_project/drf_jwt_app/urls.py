from django.urls import path
from .views import user_register, user_login, list_user,user_logout

urlpatterns = [
    path('register/', user_register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('user/', list_user, name='list_user'),
]
