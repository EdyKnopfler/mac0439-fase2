import pymongo
import datetime
import pprint

from conexao import conexao, cursor, sitedb

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
