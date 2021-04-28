from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, Table, MetaData
from decouple import config

USERNAME = config("POSTGRES_USER")
PASSWORD = config("POSTGRES_PASSWORD")
HOST = config("POSTGRES_HOST")

class DB:
    Base = declarative_base()
    engine = create_engine(f'postgresql://{USERNAME}:{PASSWORD}@{HOST}:5432/nudges')
    session = Session(engine)

    @classmethod
    def metro_query(cls, regionid: int) -> list:
        data = cls.session.query(Metro).filter(Metro.regionid == regionid)
        return [inst.get_obj() for inst in data]

    @classmethod
    def city_query(cls, regionid: int) -> list:
        data = cls.session.query(City).filter(City.regionid == regionid)
        return [inst.get_obj() for inst in data]

    @classmethod
    def zip_query(cls, regionid: int) -> list:
        data = cls.session.query(ZipCode).filter(ZipCode.regionid == regionid)
        return [inst.get_obj() for inst in data]

    @classmethod
    def county_query(cls, regionid: int) -> list:
        data = cls.session.query(County).filter(County.regionid == regionid)
        return [inst.get_obj() for inst in data]

    @classmethod
    def mapping_q(cls) -> list:
        return DB.session.query(SearchMapping).all()

class HousingTableManager:
    def date_dict(self):
        """Sets the dates and prices for eact obj"""
        data_map = {}
        for i in dir(self):
            if i[:2] == "d_":
                name = i[2:].replace("_", "-")
                data_map[name] = getattr(self, i)
        return data_map

    def get_obj(self) -> dict:
        """Returns an dict of the housing info"""
        return {
            "HouseType": self.house_type,
            "RegionID": self.regionid,
            "RegionName": self.regionname,
            "RegionType": self.regiontype,
            "StateName": self.statename,
            "pricing": self.date_dict()
        }

class Metro(DB.Base, HousingTableManager):
    __table__ = Table("metro", DB.Base.metadata, autoload=True, autoload_with=DB.engine)

class City(DB.Base, HousingTableManager):
    __table__ = Table("city", DB.Base.metadata, autoload=True, autoload_with=DB.engine)

class ZipCode(DB.Base, HousingTableManager):
    __table__ = Table("zip", DB.Base.metadata, autoload=True, autoload_with=DB.engine)

class County(DB.Base, HousingTableManager):
    __table__ = Table("county", DB.Base.metadata, autoload=True, autoload_with=DB.engine)

class SearchMapping(DB.Base):
    __table__ = Table("name_mapping", DB.Base.metadata, autoload=True, autoload_with=DB.engine)