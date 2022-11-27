import sys
sys.path.append('D:/Archivos de la U/Mis archivos/Semestre XI/Inteligencia de negocios/Proyecto/auctions_api')

from infrastructure.db.db_connection import db_connection


db = db_connection()
dataframe = db.execute("SELECT * FROM REMATES")

department = dataframe[["COD_DEP", "DEPARTAMENTO", "REGIONAL"]]
department = department.drop_duplicates()
department = department.sort_values(by=['COD_DEP'])
department.rename(columns={'COD_DEP': 'COD_DEP', 'DEPARTAMENTO': 'DEPARTMENT', 'REGIONAL': 'REGION'}, inplace=True)

town = dataframe[["COD_MUN", "MUNICIPIO", "COD_DEP"]]
town = town.drop_duplicates()
town = town.sort_values(by=['COD_MUN'])
town.rename(columns={'COD_MUN': 'COD_TOWN', 'MUNICIPIO': 'TOWN', 'COD_DEP': 'COD_DEP'}, inplace=True)

auction = dataframe[["PERIODO", "COD_MUN", "REMATES"]]
auction = auction.drop_duplicates()
auction = auction.sort_values(by=['PERIODO', 'REMATES'])
auction.rename(columns={'PERIODO': 'PERIOD', 'COD_MUN': 'COD_TOWN', 'REMATES': 'AUCTIONS'}, inplace=True)
auction.drop(auction[auction['AUCTIONS'] == 0].index, inplace=True)