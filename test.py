# -*- coding: utf-8 -*-
from pymongo import MongoClient
client = MongoClient('mongodb://santi:Santi!12321@157.245.59.56:27018/?authSource=admin&readPreference=primary&appname=MongoDB%20Compass&directConnection=true&ssl=false')
mydb = client['LPR']['timestamp']
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
        'plate':plate
    }
    result = mydb.find(query).sort('_id',-1).limit(1)
    # query = {
    #     '_id':plate
    # }

    # result = mydb.find_one(query)
    # if mydb.find_one(query) != None:
    #     print("find_one :", mydb.find_one(query))
    #     return [True,result['Line_Users_ID']]
    # else:
    #     print('find_one : False')
    #     return [False]
    for i in result:
        print(i)
result = check_plate_in_db('5กธ9147')
#5กธ9174
#print(result)
import datetime
dateNow = datetime.datetime.now()
DMY = dateNow.strftime("%d/%m/%Y")
time = dateNow.strftime('%H:%S')
print(DMY,time)