import time
from django.conf import settings


class SleepMiddleware(object):
    def __init__(self, get_response):
        try:
            self.sleep_time = settings.SLEEP_TIME
        except:
            self.sleep_time = 3
        
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        time.sleep(self.sleep_time)
        return response