from rest_framework import serializers
from .models import User, Conversation, Message

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model=User
        fields = ['id', 'username', 'phone_number', 'created_at']

class ConversationSerializer(serializers.ModelSerializer):
    participants =UserSerializer(many=True)
    class Meta:
        model = Conversation
        fields = ["created_at", "participants"]

class MessageSerializer(serializers.ModelSerializer):
    sender=UserSerializer()
    conversation = ConversationSerializer()
    class Meta:
        model =Message
        fields=["sender", "conversation", "content", "timestamp"]