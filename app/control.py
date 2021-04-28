from fastapi import FastAPI
from app.housing_api.routes import housing
from app.housing_api.id_search import DynamicNameSearch
from app.housing_api.database import DB
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.include_router(housing, prefix = "/housing")
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
    DynamicNameSearch.load_data(DB.mapping_q())