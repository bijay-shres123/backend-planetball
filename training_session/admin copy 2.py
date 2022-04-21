from django.contrib import admin
from requests import Session
from training_session import models


# Registering Requested Session Model to django admin
admin.site.register(models.RequestedSession)
