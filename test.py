# -*- coding: utf-8 -*-
from pymongo import MongoClient
client = MongoClient('mongodb://santi:Santi!12321@157.245.59.56:27018/?authSource=admin&readPreference=primary&appname=MongoDB%20Compass&directConnection=true&ssl=false')
mydb = client['LPR']['register']
def insert_id_user_line(id_user,brand,model,plate,type):
    query = {
        'id_user':id_user,
        'brand':brand,
        'model':model,
        'plate' : plate,
        'type': type,
        }
    mydb.insert_one(query)

def check_plate_in_db(plate):
    query = {
        'license_plate':plate
    }

    result = mydb.find_one(query)
    if mydb.find_one(query) != None:
        print("find_one :", mydb.find_one(query))
        return [True,result['Line_Users_ID']]
    else:
        print('find_one : False')
        return [False]
result = check_plate_in_db('5กธ9147')
#5กธ9174
print(result)