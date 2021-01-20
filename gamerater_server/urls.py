from django.conf.urls import include
from django.urls import path
from django.contrib import admin
from rest_framework import routers
from gameraterapi.views import register_user, login_user
from django.conf.urls.static import static
from django.conf import settings

from gameraterapi.views import GameViewSet, CategoryViewSet

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'games', GameViewSet, 'game')
router.register(r'categories', CategoryViewSet, 'category')


urlpatterns = [
    path('register', register_user),
    path('login', login_user),
    path('api-auth', include('rest_framework.urls', namespace='rest_framework')),
    path('', include(router.urls))
]
