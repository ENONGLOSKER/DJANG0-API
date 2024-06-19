from django.contrib import admin
from django.urls import path, include
from .views import login_page, register_page, user_list_page
# jwt
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('drf_jwt_app.urls')),
    # app
    path('', user_list_page, name='index'),
    path('user/login/', login_page, name='login'),
    path('user/register/', register_page, name='register'),
    # jwt
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
