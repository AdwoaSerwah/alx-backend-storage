#!/usr/bin/env python3
"""
Web cache and tracker module that interacts with Redis to cache HTML content
and track the number of times a page is accessed.
"""

import redis
import requests
from typing import Callable
from functools import wraps

# Create a Redis client
r = redis.Redis()


def count_calls(method: Callable) -> Callable:
    """
    Decorator that counts the number of times a method is called by
    incrementing a count key in Redis using the method's qualified name.

    Args:
        method (Callable): The method to be decorated.

    Returns:
        Callable: The wrapped function with counting logic.
    """
    @wraps(method)
    def wrapper(*args, **kwargs):
        url = args[0]  # Assume the URL is the first argument
        count_key = f"count:{url}"

        # Check if the count is cached
        cached_count = r.get(count_key)
        if cached_count is None:
            # If not cached, increment and cache the count with expiration time
            r.incr(count_key)
            r.expire(count_key, 10)  # Set expiration time for the count key
        else:
            # If cached, just increment the count
            r.incr(count_key)

        return method(*args, **kwargs)

    return wrapper


@count_calls
def get_page(url: str) -> str:
    """
    Fetches the HTML content of a page from the URL and
    caches it for 10 seconds.

    If the content is cached, it will be returned from the cache. Otherwise,
    a new request will be made to fetch the content, and
    it will be cached for 10 seconds.

    Args:
        url (str): The URL to fetch.

    Returns:
        str: The HTML content of the page.
    """
    # Check if the URL is cached
    cached_content = r.get(url)

    if cached_content:
        print(f"Cache hit for {url}")
        return cached_content.decode("utf-8")

    print(f"Cache miss for {url}")

    # Make the HTTP request to fetch the page
    response = requests.get(url)

    # Cache the result for 10 seconds using setex (expiration time 10 seconds)
    r.setex(url, 10, response.text)

    return response.text
