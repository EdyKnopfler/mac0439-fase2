import pymongo
import datetime
import pprint
import psycopg2

opcoes = "dbname='camilanaomi' user='camilanaomi' host='linux.ime.usp.br' password='zeruda0' port='5432'" #Altere essa linha! - Para alterar o DB que sera acessado
conexao = psycopg2.connect(opcoes)
cursor = conexao.cursor()
cursor.execute("SET search_path TO mac0439") #Altere essa linha - Para mudar o Schema utilizado


from pymongo import MongoClient
client = MongoClient()
client = MongoClient('localhost', 27017) #Altere essa linha - Caso você não estiver usando a porta do Mongo Default
db = client['mac0439']
sitedb = db.eAdopt

print ("All Pets:")
for pet in sitedb.find({"tipo": "pet"}):
    pprint.pprint(pet)

print ("All Requisitos:")
for req in sitedb.find({"tipo": "requisito"}):
    pprint.pprint(req)
