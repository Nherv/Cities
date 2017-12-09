# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 21:39:15 2017

@author: Hervé
"""

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date, Float
from sqlalchemy.orm import sessionmaker
from sqlalchemy import MetaData, Table
from sqlalchemy.orm import mapper
import csv


dump_database = "logement92.db"

engine = create_engine('sqlite:///{}'.format(dump_database), echo=False)
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()


class Logement92(Base):
    __tablename__ = 'static/logement92'
    insee_code = Column(String, primary_key=True)
    city = Column(String)
    housing = Column(Integer)
    main_res = Column(Integer)
    portion_hlm_tenant = Column(Float)
    social_housing = Column(Integer)

    def __init__(self, insee_code, city, housing, main_res, portion_hlm_tenant, social_housing):
        self.insee_code = insee_code
        self.city = city
        self.housing = housing
        self.main_res = main_res
        self.portion_hlm_tenant = portion_hlm_tenant
        self.social_housing = social_housing

Base.metadata.create_all(engine)

def build_db():
    outfile = open('static/logement92.csv', 'r')
    reader = csv.DictReader(outfile, delimiter=';')
    for line in reader:
        print(line['Code'])
        new_row = Logement92(
            insee_code= line['Code'],
            city = line['Libellé'],
            housing = line['Nb de logements 2014'],
            main_res = line['Nb de résidences principales 2014'],
            portion_hlm_tenant = line['Part des locataires HLM dans les rés. principales 2014'],
            social_housing = line['NB_LOGEMENTS_LOCATIFS_SOCIAUX']
            )
        session.merge(new_row)
    session.commit()
    outfile.close()

build_db()