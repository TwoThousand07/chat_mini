from django.urls import path

from .views import RoomViewSet, UserChats, EnrollToChatAPIView

from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register(r'rooms', RoomViewSet)

urlpatterns = [
    path("my_chats/", UserChats.as_view(), name="user-chats"),
    path("enroll/<slug:slug>/", EnrollToChatAPIView.as_view(), name="enroll-chat"),
] + router.urls
