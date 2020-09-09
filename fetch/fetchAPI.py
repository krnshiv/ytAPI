from googleapiclient.discovery import build 
from video.models import Video
DEVELOPER_KEY = ["AIzaSyCti-7vrJlUD9Q-jHWMgdHpdGOQMups0oU","AIzaSyCoRLuXaG2UWWAqs1m-0pF9XT1rnF-NjF4","AIzaSyAdbYv9irG-Z9yuiBMOpkVg6Aretjmngtk"] 
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"
def fetch():
    youtube_object = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey = DEVELOPER_KEY[0]) 
    search_keyword = youtube_object.search().list(q = 'football',type='video', part = "id, snippet", maxResults = 5).execute() 
    results = search_keyword.get("items", []) 
    ids=[]
    
    for vid in Video.objects.all():
        ids.append(vid.videoID)
    print(*results)
    for result in results: 
        if result['id']['kind'] == 'youtube#video':
            if result["id"]["videoId"] in ids:
                continue
            
            video = Video(videoID=result["id"]["videoId"],title=result["snippet"]["title"],description=result['snippet']['description'],published=result['snippet']['publishedAt'],thumbUrls=result['snippet']['thumbnails']['default']['url'])
            video.save()
