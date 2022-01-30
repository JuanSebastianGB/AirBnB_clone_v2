#!/usr/bin/python3
""" State Module for HBNB project """
from sqlalchemy import Column, String
from models.base_model import Base, BaseModel
from sqlalchemy.orm import relationship
from os import getenv
import models
from models.city import City


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    cities = relationship('City', backref='state', cascade='delete')
    
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        pass
    else:
        @property
        def cities(self):
            """Get cities.
            Returns the list of City instances with state_id equals to the
            current State.id"""
            cities = models.storage.all(City)
            return [city for city in cities.values()
                    if self.id == city.state_id]
