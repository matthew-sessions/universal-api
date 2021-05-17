from fastapi import FastAPI
from app.housing_api.routes import housing
# from app.drone.drone_routes import drone
from app.housing_api.id_search import DynamicNameSearch
from app.housing_api.database import DB
from fastapi.middleware.cors import CORSMiddleware
# from app.drone.video_handler import VideoRedisRecv

app = FastAPI()

app.include_router(housing, prefix = "/housing")
# app.include_router(drone, prefix="/drone")
origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



@app.on_event("startup")
async def startup():
    # VideoRedisRecv.run()
    DynamicNameSearch.load_data(DB.mapping_q())