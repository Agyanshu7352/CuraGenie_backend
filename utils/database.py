# /utils/database.py

import types
from flask_pymongo import PyMongo
from bson import ObjectId
import logging

logger = logging.getLogger(__name__)

# Global placeholder for the mongo instance
mongo = PyMongo()

logger = logging.getLogger(__name__)

# Global placeholder for the mongo instance
mongo = PyMongo()

# This is the function that will become a method
def get_user_by_id(self, user_id):
    try:
        # Note: We use 'self.db' here
        user = self.db.users.find_one({"_id": ObjectId(user_id)})
        logger.debug(f"User lookup for {user_id}: {'found' if user else 'not found'}")
        return user
    except Exception as e:
        logger.error(f"DB error while fetching user {user_id}: {e}")
        return None

# This is the main initialization function
def init_db(app):
    """Initializes the database and attaches custom methods."""
    try:
        mongo.init_app(app)
        logger.info("Successfully connected to MongoDB.")
        mongo.get_user_by_id = types.MethodType(get_user_by_id, mongo)
        logger.info("Custom method 'get_user_by_id' attached to mongo instance.")
        # --------------------------------

        # This part is optional but good practice
        app.mongo = mongo 
        return mongo
    except Exception as e:
        logger.error(f"Failed to initialize MongoDB connection: {e}")
        raise


def find_one(self, collection, query):
    """Helper method to find a document with logging"""
    logger.debug(f"Searching in {collection} with query: {query}")
    result = self.db[collection].find_one(query)
    logger.debug(f"Result found: {bool(result)}")
    return result
