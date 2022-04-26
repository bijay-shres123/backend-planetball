from django.contrib import admin
from training_session import models


# Registering Requested Session Model to django admin
admin.site.register(models.RequestedSession)
admin.site.register(models.TrainingSession)
admin.site.register(models.AskQuestion)