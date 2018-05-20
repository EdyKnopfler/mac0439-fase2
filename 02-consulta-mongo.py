import pymongo
import datetime
import pprint

print ("All Pets")
from pymongo import MongoClient
client = MongoClient()
client = MongoClient('localhost', 27017) #Altere essa linha - Caso você não estiver usandoa porta do Mongo Default
db = client['mac0439']
sitedb = db.eAdopt
for pet in sitedb.find({"tipo": "pet"}):
    pprint.pprint(pet)
