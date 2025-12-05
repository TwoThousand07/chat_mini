from django.urls import path

from .views import RoomListAPIView, RoomViewSet, UserChats

from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register(r'rooms', RoomViewSet)

urlpatterns = [
    path("my_chats/", UserChats.as_view(), name="user-chats"),
] + router.urls
