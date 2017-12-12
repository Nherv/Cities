
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date, Float
from sqlalchemy.orm import sessionmaker
from sqlalchemy import MetaData, Table
from sqlalchemy.orm import mapper
import csv


dump_database = "static/database92.db"


def load_session():
    """Connect with tables
    """
    engine = create_engine('sqlite:///{}'.format(dump_database), echo=False)
    Session = sessionmaker(bind=engine)
    session = Session()
    return session


def build_db():
    """Retrieves data from the source_database and scraping function.
    Creates rows in the table
    """
    session = load_session()
    outfile = open('static/newdata92.csv', 'r')
    reader = csv.DictReader(outfile, delimiter=';')
    for line in reader:
        print(line['Code'])
        new_row = Database(
            insee_code= line['Code'],
            city = line['Libellé'],
            nb_pharmacies = line['Nb Pharmacies et parfumerie'],
            dyn_entreprenariale = line['Dynamique Entreprenariale'],
            dyn_entr_service_commerce = line['Dynamique Entreprenariale Service et Commerce'],
            synergie_medicale = line['Synergie Médicale'],
            ind_evasion = line['Indice Evasion Client'],
            score_evasion = line['Score Evasion Client'],
            ind_synergie_medicale = line['Indice Synergie Médicale'],
            score_synergie_medicale = line['Score Synergie Médicale'],
            ind_demographique = line['Indice Démographique'],
            score_demographique = line['Score Démographique'],
            ind_menages = line['Indice Ménages'],
            score_menages = line['Score Ménages'],
            population = line['Population'],
            evo_pop = line['Evolution Population'],
            evo_pop_pourcentage = line['Evolution Population %'],
            nb_menages = line['Nb Ménages'],
            nb_res_principale = line['Nb Résidences Principales'],
            nb_proprietaire = line['Nb propriétaire'],
            nb_logements = line['Nb Logement'],
            nb_res_secondaire = line['Nb Résidences Secondaires'],
            nb_log_vacants = line['Nb Log Vacants'],
            nb_occupants_res_principale = line['Nb Occupants Résidence Principale'],
            nb_femmes = line['Nb femme'],
            nb_hommes = line['Nb Homme'],
            nb_mineurs = line['Nb Mineurs'],
            nb_majeurs = line['Nb Majeurs'],
            nb_etudiants = line['Nb Etudiants'],
            nb_entr_service = line['Nb Entreprises Secteur Services'],
            nb_entr_commerce = line['Nb Entreprises Secteur Commerce'],
            nb_entr_construction = line['Nb Entreprises Secteur Construction'],
            nb_entr_industrie = line['Nb Entreprises Secteur Industrie'],
            nb_crea_entr = line['Nb Création Entreprises'],
            nb_crea_industrie = line['Nb Création Industrielles'],
            nb_crea_construction = line['Nb Création Construction '],
            nb_crea_commerce = line['Nb Création Commerces'],
            nb_crea_service = line['Nb Création Services'],
            nb_actifs = line['Nb Actifs'],
            nb_actifs_salarie = line['Nb Actifs Salariés'],
            nb_actifs_nonsalarie = line['Nb Actifs Non Salariés'],
            nb_log_secondaires = line['Nb Logement Secondaire et Occasionnel'],
            nb_hotels = line['Nb Hotel'],
            cap_hotels = line['Capacité Hotel'],
            taux_etudiants = line['Taux Etudiants'],
            taux_propriete = line['Taux Propriété'],
            dyn_demographique = line['Dynamique Démographique'],
            cap_fiscale = line['Capacité Fiscale'],
            taux_evasion = line['Taux Evasion Client'],
            nb_edu_sante_sociale = line['Nb Education, santé, action sociale'],
            nb_service_domestiques = line['Nb Services personnels et domestiques'],
            nb_sante_action_sociale = line['Nb Santé, action sociale'],
            score_croissance_pop = line['Score Croissance Population'],
            score_croissance_entr = line['Score Croissance Entreprenariale']
            )
        session.merge(new_row)
    session.commit()
    outfile.close()
    
    outfile = open('static/population92.csv', 'r')
    reader = csv.DictReader(outfile, delimiter=';')
    for line in reader:
        print(line['Code'])
        new_row = database92(
            insee_code= line['Code'],
            city = line["Libellé"],
            pop_evo = line["Évol. annuelle moy. de la population 2009-2014"],
            population = line["Population 2014"],
            pop_25 = line["Part des pers. âgées de - de 25 ans 2014"],
            pop_25_64 = line["Part des pers. âgées de 25 à 64 ans 2014"],
            pop_65 = line["Part des pers. âgées de 65 ans ou + 2014"],
            )
        session.merge(new_row)
    session.commit()
    outfile.close()
    

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
    

    outfile = open('static/activite92.csv', 'r')
    reader = csv.DictReader(outfile, delimiter=';')
    for line in reader:
        print(line['Code'])
        new_row = Activite92(
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
