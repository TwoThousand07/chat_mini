from rest_framework import generics
from rest_framework.response import Response

from .models import Room, Message
from .serializers import RoomSerializer, MessageSerializer


class RoomListAPIView(generics.ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer