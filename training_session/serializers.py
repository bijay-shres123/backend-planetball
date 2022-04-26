from rest_framework import serializers
from training_session import models

class RequestedSessionSerializer(serializers.ModelSerializer):
    """Serializes Profile Feed Item"""

    class Meta:
        model = models.RequestedSession
        fields =  '__all__'

class TrainingSessionSerializer(serializers.ModelSerializer):
    """Serilaizer for Training Session"""

    class Meta:
        model = models.TrainingSession
        fields = '__all__'

class AskQuestionSerializer(serializers.ModelSerializer):
    """Serializes Profile Feed Item"""

    class Meta:
        model = models.AskQuestion
        fields =  '__all__'
