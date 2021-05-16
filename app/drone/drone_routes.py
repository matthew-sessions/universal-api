from fastapi import APIRouter
from app.drone.video_handler import VideoRedisRecv
from fastapi.responses import StreamingResponse


drone = APIRouter()

@drone.get("/stream")
def video_feed():
    return StreamingResponse(VideoRedisRecv.generate(), media_type= "multipart/x-mixed-replace; boundary=frame")