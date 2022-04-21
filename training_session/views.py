from training_session import models
from rest_framework import viewsets
from training_session import serializers


# ViewSet for Requested Session
class RequestedSessionViewSet(viewsets.ModelViewSet):

    """Handle creating, creating and updating requested session"""
    serializer_class = serializers.RequestedSessionSerializer
    queryset = models.RequestedSession.objects.all()
