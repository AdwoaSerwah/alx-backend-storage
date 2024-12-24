#!/usr/bin/env python3
"""
Cache module that interacts with Redis.
"""

import redis
import uuid
from typing import Union, Callable, Optional
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """
    A decorator that counts how many times a method is called.

    Args:
        method (Callable): The method to decorate.

    Returns:
        Callable: A wrapper function that increments the count
                  and calls the original method.
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """
        Wrapper function that increments the call count
        and calls the original method.
        """
        # Use the qualified name of the method for the Redis key
        key = method.__qualname__
        self._redis.incr(key)  # Increment the call count in Redis
        return method(self, *args, **kwargs)

    return wrapper


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

    @count_calls
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

    def get(self, key: str, fn: Optional[Callable] = None) -> Union[str, bytes, int, float, None]:
        """
        Retrieves data from Redis and applies an optional conversion function.

        Args:
            key (str): The key to look up in Redis.
            fn (Optional[Callable], optional): A function to convert
            the data back to its original type.

        Returns:
            Union[str, bytes, int, float, None]: The retrieved data,
            converted if necessary, or None if the key does not exist.
        """
        data = self._redis.get(key)
        if data is None:
            return None
        if fn:
            return fn(data)
        return data

    def get_str(self, key: str) -> str:
        """
        Retrieves data from Redis and converts it to a string.

        Args:
            key (str): The key to look up in Redis.

        Returns:
            str: The data converted to a string.
        """
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> int:
        """
        Retrieves data from Redis and converts it to an integer.

        Args:
            key (str): The key to look up in Redis.

        Returns:
            int: The data converted to an integer.
        """
        return self.get(key, fn=int)
