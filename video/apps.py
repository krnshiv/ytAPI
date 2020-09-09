from django.apps import AppConfig


class VideoConfig(AppConfig):
    name = 'video'

    def ready(self):
        from fetch import fetcher
        fetcher.start()