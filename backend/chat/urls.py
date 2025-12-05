from django.urls import path

from .views import RoomViewSet, UserChats, EnrollChatAPIView, ExitChatAPIView

from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register(r'rooms', RoomViewSet)

urlpatterns = [
    path("my_chats/", UserChats.as_view(), name="user-chats"),
    path("enroll/<slug:slug>/", EnrollChatAPIView.as_view(), name="enroll-chat"),
    path("exit/<slug:slug>/", ExitChatAPIView.as_view(), name="enroll-chat"),
] + router.urls
