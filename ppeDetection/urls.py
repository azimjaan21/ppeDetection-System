from django.urls import path
from .views import stream_view
from ppeDetection import views

urlpatterns = [
    path('', views.index, name='index'),
    path('stream/', stream_view, name='stream'),
]
