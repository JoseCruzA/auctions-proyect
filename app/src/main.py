import sys
sys.path.append('D:/Archivos de la U/Mis archivos/Semestre XI/Inteligencia de negocios/Proyecto/auctions_api')

from infrastructure.db.db_connection import db_connection


db = db_connection()
auctions = db.execute("SELECT * FROM REMATES").sort_values(by=['COD_DEP'])

auctions = auctions[["REGIONAL", "DEPARTAMENTO", "MUNICIPIO", "PERIODO", "REMATES"]]
auctions = auctions.drop_duplicates()
auctions.rename(columns={'REGIONAL': 'REGION', 'DEPARTAMENTO': 'DEPARTMENT', 'MUNICIPIO': 'TOWN', 'PERIODO': 'PERIOD', 'REMATES': 'AUCTIONS'}, inplace=True)
auctions.drop(auctions[auctions['AUCTIONS'] == 0].index, inplace=True)