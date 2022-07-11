# -*- coding: utf-8 -*-
"""
Created on Fri Jul  8 12:51:01 2022

@author: kenzi
"""

import sqlalchemy
from sqlalchemy import create_engine
import datetime
from data import TSL, VEML, Base
from sqlalchemy.orm import Session

def establish_connection(db_filename):
  ### set up sqlalchemy connection to sqllite dateabase
  engine = create_engine(f'sqlite:///{db_filename}.sqlite')
  conn = engine.connect()
  Base.metadata.create_all(conn)
  session = Session(bind=engine)

  return session

def query_table(table_cls):
  table = session.query(table_cls)
  return table

session=establish_connection("lux_measures")
veml_table=query_table(VEML)
tsl_table=query_table(TSL)

for row in veml_table:
  print(row.id)
  print(row.date)
  print(row.mean_lux)
  print(row.mean_light)
  
for row in tsl_table:
  print(row.id)
  print(row.date)
  print(row.mean_lux)
  print(row.mean_visible )