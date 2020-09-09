from rest_framework import serializers

class VideoSerializer(serializers.Serializer):
    videoID = serializers.CharField(max_length=120) 
    title = serializers.CharField(max_length=120)
    published = serializers.DateTimeField()
    description = serializers.CharField(max_length=120)
    thumbUrls = serializers.CharField(max_length=120)
