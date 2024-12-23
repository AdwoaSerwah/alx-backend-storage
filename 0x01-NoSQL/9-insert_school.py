#!/usr/bin/env python3
"""Module to insert a document in a collection based on kwargs"""


def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document in a collection based on kwargs.

    Args:
        mongo_collection: A pymongo collection object.
        **kwargs: Key-value pairs to insert as the document.

    Returns:
        The _id of the new document.
    """
    if mongo_collection is None:
        return None
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
