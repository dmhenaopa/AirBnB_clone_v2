#!/usr/bin/python3
""" State Module for HBNB project """
from models.city import City
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import os


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"

    if os.environ.get('HBNB_TYPE_STORAGE') == "db":
        name = Column(String(128), nullable=False)
        cities = relationship("City",
                              backref="states",
                              cascade="all, delete, delete-orphan")

    else:
        @property
        def cities(self):
            """fs getter attribute that returns City instances"""
            from models import storage
            values_city = storage.all(City)
            list_city = []
            for city in values_city.values():
                if city.state_id == self.id:
                    list_city.append(city)
            return list_city
