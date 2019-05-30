import joblib
import pymongo

timeline_goods_list = joblib.load("timeline_goods_dump.dat")

print('')
print('============ raw dataset ==============')
print(timeline_goods_list)
print('COUNT: ', len(timeline_goods_list))
print('========================================')

test_mongo_client = pymongo.MongoClient("mongodb://localhost:27017/")


# test_mongo_client.admin.add_user('test', 'test', roles=[{'role': 'readWrite', 'db': 'mall'}])

mall_db = test_mongo_client['mall']

print('')
print('===== DROP timeline_goods COLLECTION =====')
timeline_goods_collection = mall_db["timeline_goods"]
timeline_goods_collection.drop()
print(timeline_goods_collection)
print('==========================================')

print('')
print('==== CREATE timeline_goods COLLECTION ====')
timeline_goods_collection = mall_db["timeline_goods"]

print('')
print('========== insert timeline_goods =========')
x = timeline_goods_collection.insert_many(timeline_goods_list)
print(x.inserted_ids)
print('COUNT: ', len(x.inserted_ids))
print('==========================================')

