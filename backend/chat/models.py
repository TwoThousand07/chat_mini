from django.db import models
from django.contrib.auth.models import User


class Room(models.Model):
    name = models.CharField()
    slug = models.SlugField()

    def __str__(self):
        return self.name


class Message(models.Model):
    room = models.ForeignKey(
        Room, on_delete=models.CASCADE, related_name="messages")
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="messages")

    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{room.name} - {user.username}: {content[:30]}'
