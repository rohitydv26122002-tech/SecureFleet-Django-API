from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import DeviceViewSet, device_dashboard,delete_device,edit_device,user_login
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView



router = DefaultRouter()
router.register('devices', DeviceViewSet)

urlpatterns = [
    path('dashboard/', device_dashboard, name='device_dashboard'),
    path('delete/<int:device_id>/', delete_device, name='delete_device'),
    path('edit/<int:device_id>/', edit_device, name='edit_device'),
    path('login/', user_login, name='user_login'),
    path('token/', obtain_auth_token, name='api_token'),
     path('jwt/token/', TokenObtainPairView.as_view(), name='jwt_token'),
    path('jwt/refresh/', TokenRefreshView.as_view(), name='jwt_refresh'),
] + router.urls