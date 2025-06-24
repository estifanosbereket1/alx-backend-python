from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import UserSerializer, ConversationSerializer, MessageSerializer
from .models import User, Conversation, Message

# Create your views here.
class CoversationViewset(ModelViewSet):
    queryset=Conversation.objects.all()
    serializer_class=ConversationSerializer

class MessageViewSet(ModelViewSet):
    queryset=Message.objects.all()
    serializer_class=MessageSerializer

