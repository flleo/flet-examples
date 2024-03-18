import datetime
import itertools

from bson import ObjectId

from mongoDB.services import credentials as cr
import mongoDB.model.account as ac

# Get  reference to 'bank' database
db = cr.client.bank

# Get accounts collection
accounts_collection = db.accounts
id_iter = itertools.count()

na1 = ac.Account('Juan', 'checking', 0, 0, []).__dict__
na2 = ac.Account('Jose', 'checking', 100, 0, []).__dict__
na3 = ac.Account('Berta', 'checking', 1000, 0, []).__dict__
na4 = ac.Account('Fed', 'saving', 0, 100, []).__dict__
na5 = ac.Account('Maria', 'saving', 100, 100, []).__dict__
nac = [na2, na3]
nas = [na1, na2, na3, na4, na5]
df1 = {'_id': ObjectId('65f44e770672cc7e4f81161c')}
dsf = {'balance': {'$gt': 100}}
dsf2 = {'balance': {'$gt': 0}}
ref_d_to_up = df1
# d_to_up = accounts_collection.find_one(ref_d_to_up)
inc_b = {'$inc': {'balance': 50}}
# Set fields
sel_acs = {'account_type': 'saving'}
set_field = {'$inc': {'balance': 100}}
set_field2 = {'$set': {'minimum_balance': 100}}
set_field3 = {'$set': {'transfers_complete': []}}
# Delete
doc_to_del = {'balance': {'$lt': 100}}
doc_to_del2 = {'balance': {'$lt': 100}}
item_to_del = 'transfers_complete'


def find(collection, docs):
    f_docs = collection.find(docs)
    i = 0
    coll = []
    for d in f_docs:
        coll.append(d)
        print(d)
        i += 1
    print(f'Documents found: {i}')
    return coll


def find_one(collection, doc):
    re = collection.find_one(doc)
    print(re)
    return re


def insert_one(collection, doc):
    re = collection.insert_one(doc)
    inserted_id = re.inserted_id
    print(f'Id of inserted document: {inserted_id}')
    return inserted_id


def insert_many(collection, doc):
    re = collection.insert_many(doc)
    print(f'Ids of inserted documents:\n {re.inserted_ids}')
    inserted_ids = len(re.inserted_ids)
    print(f'Number of inserted documents: {inserted_ids}')
    return inserted_ids


def update_one(collection, doc, up):
    collection.update_one(doc, up)
    up_date = {'$set': {'last_updated': datetime.datetime.now()}}
    re = collection.update_one(doc, up_date)
    find_one(collection, doc)
    print(f'Documents updated: {str(re.modified_count)}')


def update_many(collection, docs, up):
    collection.update_many(docs, up)
    up_date = {'$set': {'last_updated': datetime.datetime.now()}}
    re = collection.update_many(docs, up_date)
    find(collection, docs)
    print(f'Documents matched: {str(re.matched_count)}')
    print(f'Documents updated: {str(re.modified_count)}')


def delete_item_collection(collection, item):
    coll = find(collection, [])
    for c in coll:
        if delete_one(collection, c) == 1:
            del c[item]
            insert_one(collection, c)


def delete_one(collection, doc):
    re = collection.delete_one(doc)
    print(re.deleted_count)
    print(f'Documents deleted:\n {re.deleted_count}')
    return re.deleted_count


def delete_many(collection, docs):
    re = collection.delete_many(docs)
    print(f'Documents deleted:\n {re.deleted_count}')
    return re.deleted_count


# coll = find(accounts_collection, [])
# Añade campo a colección
# update_many(accounts_collection, {}, set_field3)
# delete_item_collection(accounts_collection, item_to_del)
# delete_many(accounts_collection, {})
# update_many(accounts_collection, dsf2, set_field3)
# insert_many(accounts_collection, nas)
# update_one(accounts_collection, d_to_up, up_doc)
# find(accounts_collection, dsf)
# delete_one(accounts_collection, {'_id': ObjectId('65f4aae8c058846b07ac8436')})
find(accounts_collection, {})

cr.client.close()
