from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

# Create your models here.
class User(AbstractUser):
    email = models.EmailField(unique=True)
    password=models.CharField(max_length=128)
    user_id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    phone_number=models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)



class Conversation(models.Model):
    conversation_id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    participants = models.ManyToManyField(User, related_name='participants')
    created_at = models.DateTimeField(auto_now_add=True)


class Message(models.Model):
    message_id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    sender =models.ForeignKey(User, on_delete=models.CASCADE,related_name="sender")
    conversation =models.ForeignKey(Conversation, on_delete=models.CASCADE, related_name="conversation_id")
    message_body =models.TextField()
    sent_at=models.DateTimeField(auto_now_add=True)
