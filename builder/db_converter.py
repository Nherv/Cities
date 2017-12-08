print("allo")

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date, Float
from sqlalchemy.orm import sessionmaker
from sqlalchemy import MetaData, Table
from sqlalchemy.orm import mapper

print("allo")

dump_database = "static/population92.db"

engine = create_engine('sqlite:///{}'.format(dump_database), echo=False)
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

print("allo")

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

Base.metadata.create_all(engine)

def build_db():
    outfile = open('static/population92.csv', 'r')
    reader = csv.DictReader(outfile, delimiter=';')
    for line in reader:
        print(line["codeinsee"])
        new_row = Population92(
            insee_code= line["Code"],
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

build_db()
req = session.query(Population92).all()
print(req)
