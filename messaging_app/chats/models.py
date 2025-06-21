from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    phone_number=models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)


class Conversation(models.Model):
    participants = models.ManyToManyField(User, related_name='conversations')
    created_at = models.DateTimeField(auto_now_add=True)


class Message(models.Model):
    sender =models.ForeignKey(User, on_delete=models.CASCADE,related_name="sender")
    conversation =models.ForeignKey(Conversation, on_delete=models.CASCADE, related_name="conversation")
    content =models.TextField()
    timestamp=models.DateTimeField(auto_now_add=True)
