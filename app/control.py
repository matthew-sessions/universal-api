from fastapi import FastAPI
from app.housing_api.routes import housing
from app.housing_api.id_search import DynamicNameSearch
from app.housing_api.database import DB

app = FastAPI()

app.include_router(housing, prefix = "/housing")

@app.on_event("startup")
async def startup():
    DynamicNameSearch.load_data(DB.mapping_q())