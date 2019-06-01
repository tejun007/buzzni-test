import pymongo

from server.common.config import Config

mongo_client = pymongo.MongoClient(Config.MONGO_DB)


