# routing.py
from django.urls import path
from . import rtc_consumers,socket_consumers

websocket_urlpatterns = [
    path('ws/chat/', socket_consumers.ChatConsumer.as_asgi()),
]

# routing.py
websocket_urlpatterns += [
    path('ws/webrtc/', rtc_consumers.WebRTCSignalingConsumer.as_asgi()),
]
    