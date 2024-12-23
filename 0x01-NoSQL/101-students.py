#!/usr/bin/env python3
"""Function to return students sorted by average score from MongoDB collection"""

from pymongo import MongoClient

def top_students(mongo_collection):
    """
    Returns all students sorted by average score.

    Args:
        mongo_collection (pymongo.collection.Collection): The MongoDB collection containing student documents.

    Returns:
        list: A list of students sorted by average score, with the averageScore field added.
    """
    pipeline = [
        {
            '$project': {
                'name': 1,
                'averageScore': {
                    '$avg': '$topics.score'
                }
            }
        },
        {
            '$sort': {
                'averageScore': -1
            }
        }
    ]
    return list(mongo_collection.aggregate(pipeline))
