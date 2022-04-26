from training_session import models
from rest_framework import viewsets
from training_session import serializers
from rest_framework import filters

# ViewSet for Requested Session
class RequestedSessionViewSet(viewsets.ModelViewSet):

    """Handle creating, creating and updating requested session"""
    serializer_class = serializers.RequestedSessionSerializer
    queryset = models.RequestedSession.objects.all()

class TrainingSessionViewSet(viewsets.ModelViewSet):
    """Handle creating and updating profiles"""
    serializer_class = serializers.TrainingSessionSerializer
    queryset = models.TrainingSession.objects.all()
    
    filter_backends = (filters.SearchFilter,)
    search_fields = ('title')

# ViewSet for AskQuestion 
class AskQuestionViewSet(viewsets.ModelViewSet):

    """Handle creating, creating and updating requested session"""
    serializer_class = serializers.AskQuestionSerializer
    queryset = models.AskQuestion.objects.all()