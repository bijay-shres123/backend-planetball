from django.contrib import admin
from profiles_api import models

# Registering User Profile and Profile Feed Item to django admin
admin.site.register(models.UserProfile)
admin.site.register(models.ProfileFeedItem)