
from django.shortcuts import render ,HttpResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.pagination import api_settings
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import Video
from .serializers import VideoSerializer




class VideoView(APIView):


    def get(self,request):
        

        videos = Video.objects.order_by('published')
        paginator = Paginator(videos[::-1], 10)
        page = request.GET.get('page')

        try:
            video_details = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            video_details = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            video_details = paginator.page(paginator.num_pages)
        serializer = VideoSerializer(video_details, many=True)
        return Response(serializer.data)
    

