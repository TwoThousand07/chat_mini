from rest_framework import generics
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from .models import Room, Message
from .serializers import RoomSerializer, MessageSerializer

from django.shortcuts import get_object_or_404


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


class EnrollToChatAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, slug):
        user = request.user

        try:
            room = Room.objects.get(slug=slug)
        except Exception as e:
            return Response(f"Room does not exist. ({e})", status=status.HTTP_404_NOT_FOUND)
        
        room.members.add(user)
        return Response({"message": f"You are successfully added to chat {room.name}"}, status=status.HTTP_200_OK)
        
        
