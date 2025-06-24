from django.urls import path, include
import rest_framework.routers as routers
from rest_framework_nested.routers import NestedDefaultRouter
from .views import MessageViewSet, ConversationViewSet

router = routers.DefaultRouter()
router.register(r'conversations', ConversationViewSet, basename='conversations')

nested_router = NestedDefaultRouter(router, r'conversations', lookup='conversation')
nested_router.register(r'messages', MessageViewSet, basename='conversation-messages')

urlpatterns = [
    path('', include(router.urls)),
    path('', include(nested_router.urls)),
]
