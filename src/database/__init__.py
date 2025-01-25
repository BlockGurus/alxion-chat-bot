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
    
    #  {
    #     text: "In a world where transparency meets innovation, Alxion is your witty guide through the complexities of blockchain technology. With a touch of humor and a wealth of knowledge, she makes the digital landscape not just navigable, but downright enjoyable.",
    #     edit_history_tweet_ids: ["1883121158515466356"],
    #     id: "1883121158515466356"
    #   }
    def insert_tweet(self,tweet):
        collection = self.get_tweets_database()
        collection.insert_one(tweet)

    def close(self):
        self.client.close()