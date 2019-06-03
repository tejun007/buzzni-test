import pymongo

from server.common.config import Config

mongo_client = pymongo.MongoClient(Config.MONGO_DB)

##########################################################################
# mall db
##########################################################################
mall_db = mongo_client['mall']

##########################################################################
# mall db collections
##########################################################################
meta_collection = mall_db['meta']
timeline_goods_collection = mall_db['timeline_goods']
