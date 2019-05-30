import pymongo

from common.Config import MONGO_DB

mongo_client = pymongo.MongoClient(MONGO_DB)


