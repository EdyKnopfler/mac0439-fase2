import pymongo
import datetime
import pprint
import psycopg2

opcoes = "dbname='' user='' host='linux.ime.usp.br' password='' port='5432'" #Altere essa linha! - Para alterar o DB que sera acessado
conexao = psycopg2.connect(opcoes)
cursor = conexao.cursor()
cursor.execute("SET search_path TO mac0439") #Altere essa linha - Para mudar o Schema utilizado


from pymongo import MongoClient
client = MongoClient()
client = MongoClient('localhost', 27017) #Altere essa linha - Caso você não estiver usando a porta do Mongo Default
db = client['mac0439']
sitedb = db.eAdopt

def allPets(*args, **kwargs):
    print ("All Pets:")
    for pet in sitedb.find({"tipo": "pet"}):
        pprint.pprint(pet)
    return;

def allRequisitos(*args, **kwargs):
    print ("All Requisitos:")
    for req in sitedb.find({"tipo": "requisito"}):
        pprint.pprint(req)
    return;

# Work in Progress
def petsParaAdocao(criterios, local, raio):
    cursor.execute("""
        SELECT pet.nome, pet.especie, pet.data_nasc, pet.id_mongo_pet, usuario.lat_long
        FROM pet, anuncio, usuario
        WHERE pet.id = anuncio.id_pet AND pet.email_dono = usuario.email AND anuncio.tipo = 'Doacao' AND anuncio.status = 'Iniciado'
    """)

    print("Lista de pet para adoção em um raio de {}km do ponto {}:".format(raio, local))
    for tupla in cursor:
        latlong = tupla[4]
        latlong = latlong.replace('(', '').replace(')', '')
        latlong = latlong.split(',')
        if (abs(int(latlong[0]) - local[0]) <= raio) and (abs(int(latlong[1]) - local[1]) <= raio):
            print ("{}".format(tupla))
    return;


petsParaAdocao({"especie": "Papagaio", "raca": "Arara-azul-grande"}, [8,8], 2)
