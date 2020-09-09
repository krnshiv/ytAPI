from django.contrib import admin

from .models import Video

class VideoAdmin(admin.ModelAdmin):
    list_display = ('id','videoID','title','description','published','thumbUrls')
    list_display_links = ('id','title')
    list_filter = ('published',)
    list_per_page = 25
admin.site.register(Video, VideoAdmin)
