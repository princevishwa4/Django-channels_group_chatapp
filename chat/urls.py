from django.urls import path
from chat.views import (
    home,
    room,
)

app_name = "chat"

urlpatterns = [
    path('', home, name="home"),
    path('<str:room_name>/', room, name='room'),
]