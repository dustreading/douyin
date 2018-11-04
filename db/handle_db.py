import pymongo
from pymongo.collection import Collection

client = pymongo.MongoClient(host='47.106.120.64', port=27017)
db = client['douyin']

def handle_init_task():
    task_id_collection = Collection(db, 'task_id')
    with open('douyin_hot_id.txt', 'r') as f_share:
        for f_share_task in f_share.readlines():
            init_task = {}
            init_task['share_id'] = f_share_task.replace('\n', '')
            task_id_collection.insert_one(init_task)

def handle_get_task():
    task_id_collection = Collection(db, 'task_id')
    return task_id_collection.find_one_and_delete({})

def fans_save(fans):
    fans_collection = Collection(db, 'fans')
    fans_collection.update({'short_id':fans['short_id']}, fans, upsert=True)

def insert_to_db(user):
    user_collection = Collection(db, 'user')
    user_collection.insert_one(user)

if __name__ == '__main__':
    # handle_init_task()
    a = handle_get_task()