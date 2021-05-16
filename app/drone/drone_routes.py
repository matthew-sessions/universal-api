from fastapi import APIRouter
from app.drone.video_handler import VideoRedisRecv
from fastapi.responses import StreamingResponse
from pydantic import BaseModel

class Command(BaseModel):
    command: str
    X: int


drone = APIRouter()

@drone.get("/stream")
def video_feed():
    return StreamingResponse(VideoRedisRecv.generate(), media_type= "multipart/x-mixed-replace; boundary=frame")

@drone.get("/takeoff")
def takeoff():
    try:
        VideoRedisRecv.push(b"takeoff")
        return {"status": "ok"}
    except:
        return {"status": "failed"}

@drone.get("/land")
def land():
    try:
        VideoRedisRecv.push(b"land")
        return {"status": "ok"}
    except:
        return {"status": "failed"}

@drone.post("/post")
def command(c: Command):
    print(c.command)
    try:
        VideoRedisRecv.push(f"{c.command} {c.X}".encode())
        return {"status": "ok"}
    except:
        return {"status": "failed"}