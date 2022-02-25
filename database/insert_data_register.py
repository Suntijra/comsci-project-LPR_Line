from pymongo import MongoClient
client = MongoClient('localhost',27017)
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
# insert_id_user_line('Ufc7556c9f724503aa08f98b62d2cdb9d','5กธ9147')

def check_plate_in_db(plate):
    query = {
        'plate':plate
    }
    result = mydb.find_one(query)
    if mydb.find_one(query) !=None:
        return [True,result['id_user']]
    else:
        return [False]