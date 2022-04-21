from django.shortcuts import render
from training_session import models
from rest_framework import viewsets

from training_session import serializers
from rest_framework.authentication import TokenAuthentication

# from rest_framework import filters


class RequestedSessionViewSet(viewsets.ModelViewSet):

    """Handle creating, creating and updating profiles"""
    serializer_class = serializers.RequestedSessionSerializer
    queryset = models.RequestedSession.objects.all()

    # authentication_classes = (TokenAuthentication,)
    # permission_classes = (permissions.UpdateOwnProfile,)

    # filter_backends = (filters.SearchFilter,)
    # search_fields = ('', 'email',)

# class UserLoginApiView(ObtainAuthToken):
#    """Handle creating  authentication tokens"""
#    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES