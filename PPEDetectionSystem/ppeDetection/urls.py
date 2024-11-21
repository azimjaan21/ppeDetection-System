from django.urls import path
from .views import stream_view

urlpatterns = [
    path('video_feed/', stream_view, name='video_feed'),
]
