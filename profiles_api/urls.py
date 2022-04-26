from django import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from profiles_api import views

router = DefaultRouter()
router.register('profile',views.UserProfileViewSet)
router.register('feed',views.UserProfileFeedViewSet)
urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()),
    path('login/', views.UserLoginApiView.as_view()),
    path('', include(router.urls)),
    path('change-password/', views.ChangePasswordView.as_view(), name='change-password'),
]