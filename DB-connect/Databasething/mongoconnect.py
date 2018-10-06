from pymongo import MongoClient

connection_params = {
    'user': 'python',
    'password': '',
    'host': 'ds213832.mlab.com',
    'port': 13832,
    'namespace': 'myfirstdb',
}

connection = MongoClient(
    'mongodb://{user}:{password}@{host}:'
    '{port}/{namespace}'.format(**connection_params)
)

db = connection.myfirstdb

print(db.collection_names())
