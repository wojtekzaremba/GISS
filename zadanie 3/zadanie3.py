from pymongo import MongoClient

number = 1
tasks = []

for i in range(100):
    task = {'val':number,'res':None}
    tasks.append(task)
    number+=1

client = MongoClient()
db = client.my_db
db.tasks.insert_many(tasks)
