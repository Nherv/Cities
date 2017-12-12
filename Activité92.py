# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 23:16:15 2017

@author: Hervé
"""

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date, Float
from sqlalchemy.orm import sessionmaker
from sqlalchemy import MetaData, Table
from sqlalchemy.orm import mapper
import csv


dump_database = "static/activité92.db"

engine = create_engine('sqlite:///{}'.format(dump_database), echo=False)
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()


class Activité92(Base):
    __tablename__ = 'activité92'
    insee_code = Column(String, primary_key=True)
    city = Column(String)
    job = Column(Integer)
    act_rate_15_24 = Column(Float)
    act_rate_25_54 = Column(Float)
    act_rate_55_64 = Column(Float)
    portion_farmer = Column(Float)
    portion_craft = Column(Float)
    portion_executive = Column(Float)
    portion_worker = Column(Float)
    
    

    def __init__(self, insee_code, city, act_rate_15_24, act_rate_25_54, act_rate_55_64, portion_farmer, portion_craft, portion_executive, portion_worker):
        self.insee_code = insee_code
        self.city = city
        self.act_rate_15_24 = act_rate_15_24
        self.act_rate_25_54 = act_rate_25_54
        self.act_rate_55_64 = act_rate_55_64
        self.portion_farmer = portion_farmer
        self.portion_craft = portion_craft
        self.portion_executive = portion_executive
        self.portion_worker = portion_worker
        
Base.metadata.create_all(engine)

def build_db():
    outfile = open('static/activite92.csv', 'r')
    reader = csv.DictReader(outfile, delimiter=';')
    for line in reader:
        print(line['Code'])
        new_row = Activité92(
            insee_code= line['Code'],
            city = line['Libellé'],
            act_rate_15_24 = line["Taux d'activité des 15 à 24 ans 2014"],
            act_rate_25_54 = line["Taux d'activité des 25 à 54 ans 2014"],
            act_rate_55_64 = line["Taux d'activité des 55 à 64 ans 2014"],
            portion_farmer = line["Part des agriculteurs expl. dans le nb d’emplois au LT 2014"],
            portion_craft = line["Part des artisans, commerçants, chefs d’ent. dans le nb d’emplois au LT 2014"],
            portion_executive = line["Part des cadres et prof. intellectuelles sup. dans le nb d’emplois au LT 2014"],
            portion_worker = line["Part des ouvriers dans le nb d’emplois au LT 2014"]
            )
        session.merge(new_row)
    session.commit()
    outfile.close()

build_db()