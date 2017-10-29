# -*- coding: utf-8 -*-

# from pymongo import MongoClient
from pymongo import MongoClient

nobel_winners = [
    {
        'category': 'Physics',
        'name': 'Albert Einstein',
        'nationality': 'Swiss',
        'sex': 'male',
        'year': 1921,
    },
    {
        'category': 'Physics',
        'name': 'Paul Dirac',
        'nationality': 'British',
        'sex': 'male',
        'year': 1933
    },
    {
        'category': 'Chemistry',
        'name': 'Marie Curie',
        'nationality': 'Polish',
        'sex': 'female',
        'year': 1911
    }
]

DB_NOBEL_PRIZE = 'nobel_prize'
COLL_WINNERS = 'winners'


def create_db():
    client = MongoClient()
    db = client.nobel_prize
    coll = db.winners


def get_mongo_database(db_name, host='localhost', port=27017, username=None, password=None):

    if username and password:
        mongo_uri = 'mongodb://%s:%s@%s/%s'%(username, password, host, db_name)
        conn = MongoClient(mongo_uri)
    else:
        conn = MongoClient(host, port)
    return conn[db_name]


def show_object_id_property():
    import bson
    oid = bson.ObjectId()
    print("oid.generation_time", oid.generation_time)


def insert_data():
    db = get_mongo_database(DB_NOBEL_PRIZE)
    coll = db[COLL_WINNERS]
    coll.insert(nobel_winners)


def find_data():
    db = get_mongo_database(DB_NOBEL_PRIZE)
    collection = db[COLL_WINNERS]

    # 1. シンプルなfind()のテスト
    all = collection.find()
    res = collection.find({'category': 'Chemistry'})
    print('1. all', list(all))
    print('1. res', list(res))

    # 2. $gt(grater than)のテスト
    res = collection.find({'year': {'$gt': 1930}})
    print('2. res', list(res))


# show_object_id_property()
find_data()




