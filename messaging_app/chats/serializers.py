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

# class MessageSerializer(serializers.ModelSerializer):
#     sender=UserSerializer()
#     conversation = ConversationSerializer()
    
#     class Meta:
#         model =Message
#         fields=["sender", "conversation", "message_body", "sent_at", "message_id"]

class MessageSerializer(serializers.ModelSerializer):
    sender = UserSerializer()
    conversation = ConversationSerializer()
    message_body = serializers.CharField(max_length=1000)
    sender_full_name = serializers.SerializerMethodField()

    class Meta:
        model = Message
        fields = ["sender", "sender_full_name", "conversation", "message_body", "sent_at", "message_id"]

    def get_sender_full_name(self, obj):
        return f"{obj.sender.first_name} {obj.sender.last_name}"

    def validate_message_body(self, value):
        if len(value.strip()) < 5:
            raise serializers.ValidationError("Message is too short")
        return value