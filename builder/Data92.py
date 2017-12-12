
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date, Float
from sqlalchemy.orm import sessionmaker
from sqlalchemy import MetaData, Table
from sqlalchemy.orm import mapper
import csv


dump_database = "static/newdata92.db"

engine = create_engine('sqlite:///{}'.format(dump_database), echo=False)
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()


class Data92(Base):
    __tablename__ = 'Data92'
    insee_code = Column(String, primary_key=True)
    city = Column(String)
    nb_pharmacies = Column(Integer)
    dyn_entreprenariale = Column(Integer)
    dyn_entr_service_commerce = Column(Integer)
    synergie_medicale = Column(Integer)
    ind_evasion = Column(Float)
    score_evasion = Column(Float)
    ind_synergie_medicale = Column(Float)
    score_synergie_medicale = Column(Float)
    ind_demographique = Column(Float)
    score_demographique = Column(Float)
    ind_menages = Column(Float)
    score_menages = Column(Float)
    population = Column(Integer)
    evo_pop = Column(Integer)
    evo_pop_pourcentage = Column(Integer)
    nb_menages = Column(Integer)
    nb_res_principale = Column(Integer)
    nb_proprietaire = Column(Integer)
    nb_logements = Column(Integer)
    nb_res_secondaire = Column(Integer)
    nb_log_vacants = Column(Integer)
    nb_occupants_res_principale = Column(Integer)
    nb_femmes = Column(Integer)
    nb_hommes = Column(Integer)
    nb_mineurs = Column(Integer)
    nb_majeurs = Column(Integer)
    nb_etudiants = Column(Integer)
    nb_entr_service = Column(Integer)
    nb_entr_commerce = Column(Integer)
    nb_entr_construction = Column(Integer)
    nb_entr_industrie = Column(Integer)
    nb_crea_entr = Column(Integer)
    nb_crea_industrie = Column(Integer)
    nb_crea_construction = Column(Integer)
    nb_crea_commerce = Column(Integer)
    nb_crea_service = Column(Integer)
    nb_actifs = Column(Integer)
    nb_actifs_salarie = Column(Integer)
    nb_actifs_nonsalarie = Column(Integer)
    nb_log_secondaires = Column(Integer)
    nb_hotels = Column(Integer)
    cap_hotels = Column(Integer)
    taux_etudiants = Column(Integer)
    taux_propriete = Column(Integer)
    dyn_demographique = Column(Integer)
    cap_fiscale = Column(Integer)
    taux_evasion = Column(Integer)
    nb_edu_sante_sociale = Column(Integer)
    nb_service_domestiques = Column(Integer)
    nb_sante_action_sociale = Column(Integer)
    score_croissance_pop = Column(Float)
    score_croissance_entr = Column(Float)

    def __init__(self,
                insee_code, 
                city, 
                nb_pharmacies, 
                dyn_entreprenariale, 
                dyn_entr_service_commerce, 
                synergie_medicale,ind_evasion,
                score_evasion,
                ind_synergie_medicale,
                score_synergie_medicale,
                ind_demographique,
                score_demographique,
                ind_menages,
                score_menages,
                population,
                evo_pop,
                evo_pop_pourcentage,
                nb_menages,
                nb_res_principale,
                nb_proprietaire,
                nb_logements,
                nb_res_secondaire,
                nb_log_vacants,
                nb_occupants_res_principale,
                nb_femmes,
                nb_hommes,
                nb_mineurs,
                nb_majeurs,
                nb_etudiants,
                nb_entr_service,
                nb_entr_commerce,
                nb_entr_industrie,
                nb_crea_entr,
                nb_crea_industrie,
                nb_crea_construction,
                nb_crea_commerce,
                nb_crea_service,
                nb_actifs,
                nb_actifs_salarie,
                nb_actifs_nonsalarie,
                nb_log_secondaires,
                nb_hotels,
                cap_hotels,
                taux_etudiants,
                taux_propriete,
                dyn_demographique,
                cap_fiscale,
                taux_evasion,
                nb_edu_sante_sociale,
                nb_service_domestiques,
                nb_sante_action_sociale,
                score_croissance_pop,
                score_croissance_entr):
        self.insee_code = insee_code
        self.city = city
        self.nb_pharmacies = nb_pharmacies
        self.dyn_entreprenariale = dyn_entreprenariale
        self.dyn_entr_service_commerce = dyn_entr_service_commerce
        self.synergie_medicale = synergie_medicale
        self.ind_evasion = ind_evasion
        self.score_evasion = score_evasion
        self.ind_synergie_medicale = ind_synergie_medicale
        self.score_synergie_medicale = score_synergie_medicale
        self.ind_demographique = ind_demographique
        self.score_demographique = score_demographique
        self.ind_menages = ind_menages
        self.score_menages = score_menages
        self.population = population
        self.evo_pop = evo_pop
        self.evo_pop_pourcentage = evo_pop_pourcentage
        self.nb_menages = nb_menages
        self.nb_res_principale = nb_res_principale
        self.nb_proprietaire = nb_proprietaire
        self.nb_logements = nb_logements
        self.nb_res_secondaire = nb_res_secondaire
        self.nb_log_vacants = nb_log_vacants
        self.nb_occupants_res_principale = nb_occupants_res_principale
        self.nb_femmes = nb_femmes
        self.nb_hommes = nb_hommes
        self.nb_mineurs = nb_mineurs
        self.nb_majeurs = nb_majeurs
        self.nb_etudiants = nb_etudiants
        self.nb_entr_service = nb_entr_service
        self.nb_entr_commerce = nb_entr_commerce
        self.nb_entr_construction = nb_entr_construction
        self.nb_entr_industrie = nb_entr_industrie
        self.nb_crea_entr = nb_crea_entr
        self.nb_crea_industrie = nb_crea_industrie
        self.nb_crea_construction = nb_crea_construction
        self.nb_crea_commerce = nb_crea_commerce
        self.nb_crea_service = nb_crea_service
        self.nb_actifs = nb_actifs
        self.nb_actifs_salarie = nb_actifs_salarie
        self.nb_actifs_nonsalarie = nb_actifs_nonsalarie
        self.nb_log_secondaires = nb_log_secondaires
        self.nb_hotels = nb_hotels
        self.cap_hotels = cap_hotels
        self.taux_etudiants = taux_etudiants
        self.taux_propriete = taux_propriete
        self.dyn_demographique = dyn_demographique
        self.cap_fiscale = cap_fiscale
        self.taux_evasion = taux_evasion
        self.nb_edu_sante_sociale = nb_edu_sante_sociale
        self.nb_service_domestiques = nb_service_domestiques
        self.nb_sante_action_sociale = nb_sante_action_sociale
        self.score_croissance_pop = score_croissance_pop
        self.score_croissance_entr = score_croissance_entr
        

class Population92(Base):
    __tablename__ = 'population92'
    insee_code = Column(String, primary_key=True)
    city = Column(String)
    pop_evo = Column(Float)
    population = Column(Integer)
    pop_25 = Column(Float)
    pop_25_64 = Column(Float)
    pop_65 = Column(Float)

    def __init__(self, insee_code, city, pop_evo, population, pop_25, pop_25_64, pop_65):
        self.insee_code = insee_code
        self.city = city
        self.population = population
        self.pop_25 = pop_25
        self.pop_25_64 = pop_25_64
        self.pop_65 = pop_65
        self.pop_evo = pop_evo
     
    
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
       

class Activite92(Base):
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

