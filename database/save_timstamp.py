from pymongo import MongoClient
import  datetime

client = MongoClient('mongodb://santi:Santi!12321@157.245.59.56:27018/?authSource=admin&readPreference=primary&appname=MongoDB%20Compass&directConnection=true&ssl=false')
mydb = client['LPR']['timestamp']

def insert_licenplat(licenplat,status):
    count = mydb.count()
    dateNow = datetime.datetime.now()
    print(count)
    if count >= 200:
        Delete_ducument = mydb.find_one()
        mydb.delete_one(Delete_ducument)
    query = {
        'plate':licenplat,
        'timestamp': dateNow,
        'status':status,
        }
    mydb.insert_one(query)

# insert_licenplat('test last2','testtime')