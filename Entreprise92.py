# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 23:04:54 2017

@author: Hervé
"""

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date, Float
from sqlalchemy.orm import sessionmaker
from sqlalchemy import MetaData, Table
from sqlalchemy.orm import mapper
import csv


dump_database = "static/Entreprise92.db"

engine = create_engine('sqlite:///{}'.format(dump_database), echo=False)
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()


class Entreprise92(Base):
    __tablename__ = 'entreprise92'
    insee_code = Column(String, primary_key=True)
    city = Column(String)
    companies = Column(Integer)
    comp_creation = Column(Integer)
    comp_industry = Column(Integer)
    comp_service = Column(Integer)
    comp_sale = Column(Integer)
    comp_construction = Column(Integer)
    

    def __init__(self, insee_code, city, companies, comp_creation, comp_industry, comp_service, comp_sale, comp_construction):
        self.insee_code = insee_code
        self.city = city
        self.companies = companies
        self.comp_creation = comp_creation
        self.comp_industry = comp_industry
        self.comp_service = comp_service
        self.comp_sale = comp_sale
        self.comp_construction = comp_construction
        
Base.metadata.create_all(engine)

def build_db():
    outfile = open('static/entreprise92.csv', 'r')
    reader = csv.DictReader(outfile, delimiter=';')
    for line in reader:
        print(line['Code'])
        new_row = Entreprise92(
            insee_code= line['Code'],
            city = line['Libellé'],
            companies = line['Nb entreprises 2016'],
            comp_creation = line["Nb créations d'entreprises 2016"],
            comp_industry = line["Nb ent. dans l'industrie 2016"],
            comp_service = line["Nb ent. dans les services marchands 2016"],
            comp_sale = line["Nb ent. dans le commerce, transports, hébergement, restauration 2016"],
            comp_construction = line["Nb ent. dans la construction 2016"]
            )
        session.merge(new_row)
    session.commit()
    outfile.close()

build_db()