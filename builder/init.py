from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import sessionmaker
from sqlalchemy import MetaData, Table
from sqlalchemy.orm import mapper
from builder.base import *
import csv

dump_database = "static/database.db"

def main():
	# Empty and reset table cities 
	engine = create_engine('sqlite:///{}'.format(dump_database), echo=False)
	Base.metadata.drop_all(engine)

	# Create a .csv file in /export/
	new_file2 = open('export/database.csv', 'w')
	outcsv = csv.writer(new_file2)
	outcsv.writerow([c.name for c in Cities.__table__.columns])
	new_file2.close()