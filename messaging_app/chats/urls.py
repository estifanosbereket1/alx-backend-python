from django.urls import path, include
import rest_framework.routers as routers
from .views import MessageViewSet, ConversationViewSet

router = routers.DefaultRouter() 

router.register(r'messages', MessageViewSet)
router.register(r'conversations', ConversationViewSet)

urlpatterns = router.urls