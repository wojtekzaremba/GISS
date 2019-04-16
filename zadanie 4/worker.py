from pymongo import MongoClient
from random import randint
from time import sleep



def calc(val):
    time = randint(1,2)
    sleep(time)
    return val * val


client  = MongoClient()
db = client.my_db


while True:
    current_document = db.tasks.find_one({'res':None})
    if current_document is not None:
        value = current_document['val']
        value = calc(value)
        current_document = db.tasks.update_one({'_id' : current_document['_id']},{ '$set': { 'res' : value } })

    else:
        break
