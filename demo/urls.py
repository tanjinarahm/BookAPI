# from django.contrib import admin
# from . import views
from django.urls import path, include
from rest_framework import routers
from .views import BookViewSet

router = routers.DefaultRouter()
router.register('books', BookViewSet)

urlpatterns = [
    # path('first', views.first),
    path('', include(router.urls))
]