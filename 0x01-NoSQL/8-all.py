#!/usr/bin/env python3
"""Module to list all documents in a collection"""

def list_all(mongo_collection):
    """
    Lists all documents in a collection.
    
    Args:
        mongo_collection: A pymongo collection object.
    
    Returns:
        A list of documents in the collection, or an empty list if none exist.
    """
    if mongo_collection is None:
        return []
    return list(mongo_collection.find())
