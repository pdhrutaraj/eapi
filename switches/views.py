from rest_framework import viewsets, permissions
from .models import Switch
from .serializers import SwitchSerializer

class SwitchViewSet(viewsets.ModelViewSet):
    queryset = Switch.objects.all()
    serializer_class = SwitchSerializer
    permission_classes = [permissions.IsAdminUser]  # Only superusers can manage switches

