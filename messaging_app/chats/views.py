from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import UserSerializer, ConversationSerializer, MessageSerializer
from .models import User, Conversation, Message
from rest_framework import status, filters

# Create your views here.
class ConversationViewSet(ModelViewSet):
    queryset=Conversation.objects.all()
    serializer_class=ConversationSerializer

class MessageViewSet(ModelViewSet):
    queryset=Message.objects.all()
    serializer_class=MessageSerializer

