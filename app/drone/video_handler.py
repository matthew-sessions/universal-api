import redis
import threading
from decouple import config

IP = config("IP")

class VideoRedisRecv:
    client = redis.Redis(host=IP, port = 6379)
    p = client.pubsub()
    p.subscribe('dev')
    FRAME = None
    THREAD = None

    @classmethod
    def _collect_video(cls):
        while True:
            message = cls.p.get_message()
            if message and message["data"] != 1:
                cls.FRAME = message["data"]

    @classmethod
    def generate(cls):
        while True:
            if not cls.FRAME:
                continue
            
            yield cls.FRAME

    @classmethod
    def run(cls):
        cls.THREAD = threading.Thread(target=cls._collect_video)
        cls.THREAD.daemon = True
        cls.THREAD.start()