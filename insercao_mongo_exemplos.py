import pymongo
import datetime
import pprint
from bson.objectid import ObjectId

from pymongo import MongoClient
client = MongoClient()
client = MongoClient('localhost', 27017) #Altere essa linha - Caso você não estiver usando a porta do Mongo Default
db = client['mac0439']
sitedb = db.eAdopt

def insertMongoPet(nomePet):
    if nomePet == "John":
        new_pet = {"tipo": "pet",
                     "raca": "Labrador",
                     "cor_pelo": "Marrom",
                     "peso": 24.5,
                     "vacina": [{"descricao": "v8", "data": datetime.datetime(2013, 11, 10)}]
                    }
    elif nomePet == "Loro":
        new_pet = {"tipo": "pet",
                     "raca": "Arara-azul-grande",
                     "cor_pena": "Azul"
                    }
    elif nomePet == "Luke":
        new_pet = {"tipo": "pet",
                     "raca": "Siames",
                     "cor_pelo": "Preto/Branco",
                     "alimento": [{"descricao": "Peixe Cru", "motivo": "Se recusa a comer outra coisa"}],
                     "necessidade": ["Precisa andar bastante ou fica raivoso"]
                    }
    elif nomePet == "Tana":
        new_pet = {"tipo": "pet",
                     "raca": "Coral-Falsa",
                     "cor_escamas": "Vermelho/Branco/Preto",
                     "necessidade": ["Viver num ambiente climatizado"]
                    }
    elif nomePet == "Azuril":
        new_pet = {"tipo": "pet",
                     "raca": "Beta",
                     "cor_escamas": "Roxo/Azul/Preto",
                     "necessidade": ["Aquario sem nenhum peixe que ele possa comer"],
                     "tamanhoTextual": "medio"
                    }
    elif nomePet == "Ol":
        new_pet = {"tipo": "pet",
                     "raca": "Golden Retriver",
                     "cor_pelo": "Dourado",
                     "peso": 20.6,
                     "alimento": [{"descricao": "Ração Premium"}],
                     "necessidade": ["Pelo tem que ser cortado a cada semana", "Faz treino três vezes por semana"],
                     "vacina": [{"descricao": "v8", "data": datetime.datetime(2017, 6, 30)}, {"descricao": "v10", "data": datetime.datetime(2016, 9, 9)}]
                     }
    else:
        new_pet = {"tipo": "pet",
                     "raca": "Unknown"
                    }
    result = sitedb.insert_one(new_pet)
    return str(result.inserted_id)

def insertMongoRequisito(tituloReq):
    if tituloReq == "Janelas":
        new_req = {"tipo": "requisito",
                   "descricao": "O Loro gosta de voar, se a janela nao tiver tela ele vai fugir"
                  }
    elif tituloReq == "Alpiste":
        new_req = {"tipo": "requisito",
                   "descricao": "A comida de preferência do Loro é Alpiste Frances, mas se tiver outro não tem problema"
                  }
    elif tituloReq == "Pelo":
        new_req = {"tipo": "requisito",
                   "descricao": "Preciso de um cachorro preto para cruzar com o meu Golden dourado"
                  }
    elif tituloReq == "Raca":
        new_req = {"tipo": "requisito",
                   "descricao": "Seria ideal um cachorro da mesma raca que o John, mas desde que eles possam cruzar sem problemas"
                  }
    else:
        new_req = {"tipo": "requisito",
                   "descricao": "Unknown"
                   }
    result = sitedb.insert_one(new_req)
    return str(result.inserted_id)
