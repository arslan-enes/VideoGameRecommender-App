from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
import os

load_dotenv()


def get_database():
    uri = os.getenv("MONGODB_CONNECTION_STRING")
    # Create a new client and connect to the server
    client = MongoClient(uri, server_api=ServerApi('1'))

    return client['VideoGames']

if __name__ == "__main__":
    db_name = get_database()
