# -*- coding: utf-8 -*-
"""base_models.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ymb6Aa_2LGax0sUJ8lRCyg6AwQpnIOgw
"""

from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

# Import modules to declare columns and column data types
from sqlalchemy import Column, Integer, DateTime, String, Float

### Data Model

class VEML(Base):
    __tablename__ = 'veml'
    id = Column(Integer, primary_key=True)
    date = Column(DateTime)
    mean_lux = Column(Float)
    min_lux = Column(Float)
    max_lux = Column(Float)
    variance_lux = Column(Float)
    mean_light = Column(Float)
    min_light = Column (Integer)
    max_light = Column(Integer)
    variance_light = Column(Float)

class TSL(Base):
    __tablename__ = 'tsl'
    id = Column(Integer, primary_key=True)
    date = Column(DateTime)
    mean_lux = Column(Float)
    min_lux = Column(Float)
    max_lux = Column(Float)
    variance_lux = Column(Float)
    mean_visible = Column(Float)
    min_visible = Column(Integer)
    max_visible = Column(Integer)
    variance_visible = Column(Float)