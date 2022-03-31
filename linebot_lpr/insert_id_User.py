from pymongo import MongoClient
client = MongoClient('localhost',27017)
mydb = client['mydb']['id_user']
def insert_id_user_line(id_user):
    query = {'id':id_user}
    mydb.insert_one(query)
