from rest_framework import viewsets, permissions
from rest_framework.authentication import BasicAuthentication, SessionAuthentication, TokenAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Mission
from .serializers import MissionSerializer

# Base ViewSet with full CRUD capabilities
class BaseMissionViewSet(viewsets.ModelViewSet):
    queryset = Mission.objects.all().order_by('-deadline')
    serializer_class = MissionSerializer

# 1. No Auth Version
class MissionNoAuthViewSet(BaseMissionViewSet):
    authentication_classes = []
    permission_classes = [permissions.AllowAny]

# 2. Basic Auth Version
class MissionBasicAuthViewSet(BaseMissionViewSet):
    authentication_classes = [BasicAuthentication]
    permission_classes = [permissions.IsAuthenticated]

# 3. Session Auth Version
class MissionSessionAuthViewSet(BaseMissionViewSet):
    authentication_classes = [SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]

# 4. Token Auth Version
class MissionTokenAuthViewSet(BaseMissionViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

# 5. JWT Auth Version
class MissionJWTAuthViewSet(BaseMissionViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]