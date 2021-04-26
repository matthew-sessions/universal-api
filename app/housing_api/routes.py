from fastapi import APIRouter
from app.housing_api.database import DB
from app.housing_api.id_search import DynamicNameSearch

housing = APIRouter()

@housing.get("/metro/{region_id}")
def metro(region_id):
    data = DB.metro_query(region_id)
    return {"message": data}

@housing.get("/city/{region_id}")
def metro(region_id):
    data = DB.city_query(region_id)
    return {"message": data}

@housing.get("/zipcode/{region_id}")
def metro(region_id):
    data = DB.zip_query(region_id)
    return {"message": data}

@housing.get("/county/{region_id}")
def metro(region_id):
    data = DB.county_query(region_id)
    return {"message": data}

@housing.get("/search/{term}")
def search(term):
    print(term)
    return {
        "results": DynamicNameSearch.search(term)
    }