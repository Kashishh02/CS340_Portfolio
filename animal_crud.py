from pymongo import MongoClient
from pymongo.errors import PyMongoError


class AnimalShelter:
    """
    CRUD class for the aac.animals collection.
    This Codio environment allows local Mongo connections without authentication.
    """

    def __init__(self, username=None, password=None,
                 host="localhost",
                 port=27017,
                 db_name="aac",
                 collection_name="animals"):

        self.client = None
        self.db = None
        self.collection = None

        try:
            # No-auth local connection
            uri = f"mongodb://{host}:{port}/{db_name}"
            self.client = MongoClient(uri)
            self.db = self.client[db_name]
            self.collection = self.db[collection_name]

            # quick ping to confirm connection
            self.client.admin.command("ping")
            print("MongoDB connected (no-auth local connection).")

        except PyMongoError as e:
            print("Mongo connection failed:", e)


    def create(self, data):
        if data is None or type(data) is not dict or len(data) == 0:
            return False
        try:
            result = self.collection.insert_one(data)
            return result.acknowledged
        except PyMongoError as e:
            print("Create failed:", e)
            return False


    def read(self, query, projection=None):
        if self.collection is None:
            print("Read failed: No Mongo collection available (connection failed).")
            return []

        if query is None:
            query = {}
        if type(query) is not dict:
            return []

        try:
            cursor = self.collection.find(query, projection)
            return list(cursor)
        except PyMongoError as e:
            print("Read failed:", e)
            return []


    def update(self, query, update_data):
        if self.collection is None:
            print("Update failed: No Mongo collection available (connection failed).")
            return 0

        if type(query) is not dict or type(update_data) is not dict or len(update_data) == 0:
            return 0

        if any(key.startswith("$") for key in update_data.keys()):
            update_doc = update_data
        else:
            update_doc = {"$set": update_data}

        try:
            result = self.collection.update_many(query, update_doc)
            return result.modified_count
        except PyMongoError as e:
            print("Update failed:", e)
            return 0


    def delete(self, query):
        if self.collection is None:
            print("Delete failed: No Mongo collection available (connection failed).")
            return 0

        if type(query) is not dict or len(query) == 0:
            return 0

        try:
            result = self.collection.delete_many(query)
            return result.deleted_count
        except PyMongoError as e:
            print("Delete failed:", e)
            return 0
