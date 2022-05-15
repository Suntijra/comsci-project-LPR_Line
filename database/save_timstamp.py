from pymongo import MongoClient
import  datetime
client = MongoClient('mongodb://santi:Santi!12321@157.245.59.56:27018/?authSource=admin&readPreference=primary&appname=MongoDB%20Compass&directConnection=true&ssl=false')
mydb = client['LPR']['timestamp']
query = {
            'plate':'licenplat',
            'DMY': 'DMY',
            "time":'time',
            'status':'status',
            }
mydb.insert_one(query)
def insert_licenplat(licenplat,status):
    x = mydb.find().sort('_id',-1).limit(1)
    for plate_data in x :
        plate_db = plate_data
    print('Input :',licenplat)
    print('mongodb :',plate_db['plate'])
  
    if licenplat == plate_db['plate']:
        print('plate : ซ้ำๆ')
        return False
    else:
        count = mydb.count()
        dateNow = datetime.datetime.now()
        DMY = dateNow.strftime("%d/%m/%Y")
        time = dateNow.strftime('%H:%M')
        print(count)
        if count >= 1000:
            Delete_ducument = mydb.find_one()
            mydb.delete_one(Delete_ducument)
        query = {
            'plate':licenplat,
            'DMY': DMY,
            "time":time,
            'status':status,
            }
        mydb.insert_one(query)
        return True

# insert_licenplat('test last2','testtime')