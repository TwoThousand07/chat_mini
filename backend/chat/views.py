from rest_framework import generics
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Room, Message
from .serializers import RoomSerializer, MessageSerializer


class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.prefetch_related("members").all()
    serializer_class = RoomSerializer
    lookup_field = "slug"
    

class UserChats(generics.ListAPIView):
    def get_queryset(self):
        user = self.request.user

        return Room.objects.prefetch_related("members").filter(members=user)
    
    serializer_class = RoomSerializer
    permission_classes = [IsAuthenticated]