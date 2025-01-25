from pymongo import MongoClient
from dotenv import load_dotenv
import certifi
import os
load_dotenv()
class Database:
    def __init__(self):
        self.client = MongoClient(os.getenv("MONGO_URI"),tlsCAFile=certifi.where())

    def get_tweets_database(self):
        return self.client['alxion_bot']['tweet_ids']

    # def get_tweet_ids(self):
    #     collection = self.get_tweets_database()
    #     return collection.find()
    
    def insert_tweet_id(self,tweet_id):
        collection = self.get_tweets_database()
        collection.insert_one({"tweet_id":tweet_id})

    def close(self):
        self.client.close()