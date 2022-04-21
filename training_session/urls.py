from django import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from training_session import views

router = DefaultRouter()
router.register('request_session',views.RequestedSessionViewSet)

urlpatterns = [
    path('', include(router.urls)),
    
]