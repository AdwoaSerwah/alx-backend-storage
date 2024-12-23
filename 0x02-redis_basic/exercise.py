#!/usr/bin/env python3
"""
Cache module that interacts with Redis.
"""

import redis
import uuid
from typing import Union


class Cache:
    """
    Cache class for handling Redis operations.
    """

    def __init__(self):
        """
        Initializes a Cache instance and connects to Redis.
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Stores the input data in Redis with a random key.

        Args:
            data (Union[str, bytes, int, float]): The data to store in Redis.

        Returns:
            str: The generated Redis key.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
