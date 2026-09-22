from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from missions.views import (
    MissionNoAuthViewSet,
    MissionBasicAuthViewSet,
    MissionSessionAuthViewSet,
    MissionTokenAuthViewSet,
    MissionJWTAuthViewSet
)

# Set up routers for each auth version
r_no_auth = DefaultRouter()
r_no_auth.register(r'missions', MissionNoAuthViewSet, basename='no-auth-mission')

r_basic = DefaultRouter()
r_basic.register(r'missions', MissionBasicAuthViewSet, basename='basic-mission')

r_session = DefaultRouter()
r_session.register(r'missions', MissionSessionAuthViewSet, basename='session-mission')

r_token = DefaultRouter()
r_token.register(r'missions', MissionTokenAuthViewSet, basename='token-mission')

r_jwt = DefaultRouter()
r_jwt.register(r'missions', MissionJWTAuthViewSet, basename='jwt-mission')

urlpatterns = [
    path('admin/', admin.site.urls),

    # DRF Session authentication endpoints
    path('api-auth/', include('rest_framework.urls')),

    # Token Authentication login endpoint
    path('api/v1/token-auth/login/', obtain_auth_token, name='api_token_auth'),

    # JWT Authentication login endpoints
    path('api/v1/jwt/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/jwt/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Versioned API Routes
    path('api/v1/no-auth/', include(r_no_auth.urls)),
    path('api/v1/basic/', include(r_basic.urls)),
    path('api/v1/session/', include(r_session.urls)),
    path('api/v1/token/', include(r_token.urls)),
    path('api/v1/jwt/', include(r_jwt.urls)),
]