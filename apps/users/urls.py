from rest_framework.routers import DefaultRouter
from django.urls import path,include

from apps.users.views.auth import LoginViewSet
from apps.users.views.profile import ProfileViewSet

router = DefaultRouter()
router.register('', LoginViewSet, basename='login')
router.register('',ProfileViewSet, basename='profile')

urlpatterns = [
    path('',view=include(router.urls)),
]
