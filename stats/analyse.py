import pandas as pd
import sqlalchemy
import csv
import requests
from bs4 import BeautifulSoup
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import sessionmaker
from sqlalchemy import MetaData, Table
from sqlalchemy.orm import mapper
import re
import unidecode
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import matplotlib.pyplot as plt
import numpy as np
import math
from builder.base import *


######### Input #########
dump_database = "static/database.db"
#########################

color = dict()
color['PCF'] = "#800000"
color['FG'] = "#800000"
color['PS'] = "#FF0000"
color['DVG'] = "#FF6564"
color['PRG'] = "#F79295"
color['EELV'] = "#1DCD40"
color['MoDem'] = "#9F66C2"
color['UDI'] = "#9F66C2"
color['DVD'] = "#9EA0FF"
color['UMP-LR'] = "#0000FF"
color['FN'] = "#000080"
color['NA'] = "#000000"
color['SE'] = "#E8ECC1"


engine = create_engine('sqlite:///{}'.format(dump_database), echo=False)
Session = sessionmaker(bind=engine)
session = Session()


def builder():
    """Build panda statframe
    """
    df = pd.DataFrame(session.query(Cities.__table__).all())
    return df


def city_map(df):
    """Draw map of the cities with the color of their party
    """
    Latitudes = df.as_matrix(columns=df.columns[4:5])
    Longitudes = df.as_matrix(columns=df.columns[5:6])
    Partys = df.as_matrix(columns=df.columns[10:11])

    fig, ax = plt.subplots()
    for i in range(0, len(Latitudes)):
        if Latitudes[i][0] == "None":
            latitude = (-np.cos(48.8 * np.pi / 180))
        else:
            latitude = -np.cos(float(Latitudes[i][0]) * np.pi / 180)

        if Longitudes[i][0] == "None":
            longitude = np.sin(2.02 * np.pi / 180)
        else:
            longitude = np.sin(float(Longitudes[i][0]) * np.pi / 180)

        colour = color[Partys[i][0]]

        ax.scatter(longitude, latitude, c=colour, alpha=0.8, edgecolors='none')

    plt.show()


def new_companies_rate(df):
    df["new_companies_rate"] = df["newcompanies2016"]/df["companies2016"]
    df = df.sort_values(["new_companies_rate"])
    print(df)


def main(arg):
    #assert arg in ['pop_per_party', 'party_vs_citysize1', 'party_vs_citysize2','city_map'], \
    #       'Argument is not one of pop_per_party, party_vs_citysize1, party_vs_citysize2, city_map: ' + arg
    df = builder()
    if arg == "city_map":
        city_map(df)
    else :
        new_companies_rate(df)