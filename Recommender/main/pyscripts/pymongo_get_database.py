from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
import os


try: 
    load_dotenv()
    uri = os.getenv("MONGODB_CONNECTION_STRING")
    client = MongoClient(uri, server_api=ServerApi('1'))
    video_games = client["VideoGames"]
    print("Connected to MongoDB Atlas cluster!")
except Exception as e:
    print("Error connecting to MongoDB Atlas cluster:\n", e)




def get_database():
    # Create a new client and connect to the server
    return video_games

if __name__ == "__main__":
    db_name = get_database()
