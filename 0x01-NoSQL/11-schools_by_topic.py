#!/usr/bin/env python3
"""Module to find schools by topic"""


def schools_by_topic(mongo_collection, topic):
    """
    Returns the list of schools having a specific topic.

    Args:
        mongo_collection: A pymongo collection object.
        topic (str): The topic to search for.

    Returns:
        list: A list of documents matching the topic.
    """
    if mongo_collection is None:
        return []
    return list(mongo_collection.find({"topics": topic}))
