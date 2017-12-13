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

    
def calcul_indicateurs(ville):
    indicateurs = df.loc['ville', ['taux_propriete', 'ind_menages','nb_log_vacants','evo_pop', 'nb_pharmacies','population','nb_mineurs','nb_majeurs','cap_fiscale','nb_femmes','nb_hommes','nb_log_vacants','nb_res_secondaire']]
    
    indicateurs['acces_prop'] = indicateurs['taux_propriete']/indicateurs['ind_menages']
    
    indicateurs['pb_logement'] = (indicateurs['nb_log_vacants']-indicateurs['evo_pop'])/indicateurs['evo_pop']
    
    indicateurs['densite_pharma'] = indicateurs['nb_pharmacies']/indicateurs['pop']
    
    indicateurs['parite'] = (indicateurs['nb_femmes']-indicateurs['nb_hommes'])/indicateurs['nb_hommes']
    
    indicateurs['jeunesse_pop'] = indicateurs['nb_mineurs']/indicateurs['population']
    
    indicateurs['majeurs_pop'] = indicateurs['nb majeurs']/indicateurs['population']
    
    indicateurs['logement_principal'] = (indicateurs['nb_log_vacants']-indicateurs['nb_res_secondaire'])/indicateurs['nb_res_secondaire']
    
    print(indicateurs)
