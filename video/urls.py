from django.urls import path

from .views import VideoView

app_name = 'video'

urlpatterns = [
    path('videos/', VideoView.as_view()),
]