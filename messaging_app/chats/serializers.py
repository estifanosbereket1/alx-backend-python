from rest_framework import serializers
from .models import User, Conversation, Message

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model=User
        fields = ['user_id', 'first_name', 'last_name', 'email', 'phone_number']

class ConversationSerializer(serializers.ModelSerializer):
    participants =UserSerializer(many=True)
    class Meta:
        model = Conversation
        fields = ["conversation_id", "created_at", "participants"]

class MessageSerializer(serializers.ModelSerializer):
    sender=UserSerializer()
    conversation = ConversationSerializer()
    class Meta:
        model =Message
        fields=["sender", "conversation", "message_body", "sent_at", "message_id"]