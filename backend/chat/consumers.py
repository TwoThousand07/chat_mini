import json

from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async

from django.contrib.auth.models import User

from .models import Message, Room


class ChatAsyncWebsocketConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = f'chat_{self.room_name}'

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def receive(self, text_data=None, bytes_data=None):
        text_data_json = json.loads(text_data)
        content = text_data_json["message"]
        user = self.scope["user"]
        
        if user.is_authenticated:
            await self._save_message(self.room_name, user, content)

            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    "type": "chat_message",
                    "message": content,
                    "user": user.username
                }
            )
        else:
            await self.send(json.dumps({"error": "User is not authenticated."}))

    async def disconnect(self, code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def chat_message(self, event):
        message = event["message"]
        user = event["user"]
        
        await self.send(json.dumps({
            "message": message,
            "user": user
        }))

    @database_sync_to_async
    def _save_message(self, room_name, user, content):
        room, created = Room.objects.get_or_create(name=room_name, defaults={"slug": room_name})
        message = Message.objects.create(
            room=room, user=user, content=content)
        return message
    
