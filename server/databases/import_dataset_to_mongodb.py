import os

import joblib
import pymongo

from server.common.config import Config

dump_data_dir = os.path.dirname(os.path.abspath(__file__))
timeline_goods_list = joblib.load(dump_data_dir + "/timeline_goods_dump.dat")

# refining data row for timeline_goods collection
timeline_goods_list = [dict(_id=good['id'],
                            mall_name=good['genre2'],
                            name=good['name'],
                            img=good['img'],
                            url=good['url'],
                            cate1=good['cate1'],
                            date=good['date'],
                            start_time=good['start_time'],
                            end_time=good['end_time'],
                            org_price=good['org_price'],
                            price=good['price'])
                       for good in timeline_goods_list]

print('')
print('============ raw dataset ==============')
print(timeline_goods_list)
print('COUNT: ', len(timeline_goods_list))
print('========================================')

test_mongo_client = pymongo.MongoClient(Config.MONGO_DB)

# test_mongo_client.admin.add_user('test', 'test', roles=[{'role': 'readWrite', 'db': 'mall'}])

mall_db = test_mongo_client['mall']

print('')
print('===== DROP meta & timeline_goods  COLLECTION =====')
timeline_goods_collection = mall_db["timeline_goods"]
timeline_goods_collection.drop()

meta_collection = mall_db["meta"]
meta_collection.drop()

print(timeline_goods_collection)
print(meta_collection)
print('==========================================')

print('')
print('==== CREATE meta & timeline_goods COLLECTION ====')
timeline_goods_collection = mall_db["timeline_goods"]
timeline_goods_collection.create_index('mall_name', background=True)
timeline_goods_collection.create_index('cate1', background=True)
timeline_goods_collection.create_index('end_time', background=True)
timeline_goods_collection.create_index('date', background=True)
timeline_goods_collection.create_index('start_time', background=True)
timeline_goods_collection.create_index('end_time', background=True)

meta_collection = mall_db["meta"]
print('==========================================')

print('')
print('========== insert timeline_goods =========')
x = timeline_goods_collection.insert_many(timeline_goods_list)
print(x.inserted_ids)
print('COUNT: ', len(x.inserted_ids))
print('==========================================')

print('')
print('========== insert meta data =========')
timeline_goods_dates = timeline_goods_collection \
    .distinct('date', {'$and': [{'date': {'$ne': None}},
                                     {'date': {'$ne': 0}},
                                     {'date': {'$exists': True}}]})
timeline_goods_mall_names = timeline_goods_collection \
    .distinct('mall_name', {'$and': [{'mall_name': {'$ne': None}},
                                     {'mall_name': {'$ne': ''}},
                                     {'mall_name': {'$exists': True}}]})
timeline_goods_cate1s = timeline_goods_collection \
    .distinct('cate1', {'$and': [{'cate1': {'$ne': None}},
                                 {'cate1': {'$ne': ''}},
                                 {'cate1': {'$exists': True}}]})
print('mall_names', timeline_goods_mall_names)
print('goods_cate1s', timeline_goods_cate1s)
insert_filters = meta_collection.insert({'timeline_filters': {
    'dates': timeline_goods_dates,
    'mall_names': timeline_goods_mall_names,
    'cate1s': timeline_goods_cate1s
}})
print(insert_filters)
print('==========================================')
