import psycopg2
from pymongo import MongoClient

#Altere essa linha! - Para alterar o DB que sera acessado
opcoes = "dbname='' user='' host='linux.ime.usp.br' password='' port='5432'"
conexao = psycopg2.connect(opcoes)
cursor = conexao.cursor()
#Altere essa linha - Para mudar o Schema utilizado
cursor.execute("SET search_path TO mac0439") 

client = MongoClient()
#Altere essa linha - Caso você não estiver usando a porta do Mongo Default
client = MongoClient('localhost', 27017) 
db = client['mac0439']
sitedb = db.eAdopt
