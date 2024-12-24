#!/usr/bin/env python3
"""
Web caching and tracker module
"""

import redis
import requests
from typing import Callable

redis_client = redis.Redis()


def get_page(url: str) -> str:
    """
    Fetches the HTML content of a URL and caches it.
    Tracks the number of times the URL is accessed.

    Args:
        url (str): The URL to fetch.

    Returns:
        str: The HTML content of the URL.
    """
    count_key = f"count:{url}"
    cache_key = f"cached:{url}"

    # Increment the count for the URL
    redis_client.incr(count_key)

    # Check if content is already cached
    cached_content = redis_client.get(cache_key)
    if cached_content:
        return cached_content.decode("utf-8")

    # Fetch content from the URL
    response = requests.get(url)
    html_content = response.text

    # Cache the content with a 10-second expiration
    redis_client.setex(cache_key, 10, html_content)
    return html_content
