from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MessageViewSet, ConversationViewSet

routers = DefaultRouter()

routers.register(r'messages', MessageViewSet)
routers.register(r'conversations', ConversationViewSet)

urlpatterns = routers.urls
