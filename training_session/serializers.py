from rest_framework import serializers
from training_session import models

class RequestedSessionSerializer(serializers.ModelSerializer):
    """Serializes Profile Feed Item"""

    class Meta:
        model = models.RequestedSession
        fields =  '__all__'
     