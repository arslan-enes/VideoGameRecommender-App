from .pymongo_get_database import get_database

dbname = get_database()
collection_name = dbname["MetacriticPCGamesofAllTime"]


def get_documents(document_ids):
    recommended_docs = collection_name.find({"_id":{"$in": document_ids}})
    return recommended_docs