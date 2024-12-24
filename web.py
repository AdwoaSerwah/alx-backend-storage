#!/usr/bin/env python3
"""
Web caching module with Redis.
"""

import redis
import requests
from typing import Callable

redis_client = redis.Redis()


def get_page(url: str) -> str:
    """
    Fetches the HTML content of a URL and caches it in Redis.
    Also tracks the number of times the URL is accessed.

    Args:
        url (str): The URL to fetch.

    Returns:
        str: The HTML content of the URL.
    """
    cache_key = f"count:{url}"
    html_key = f"html:{url}"

    # Increment the access count for the URL
    redis_client.incr(cache_key)

    # Check if the URL content is already cached
    cached_html = redis_client.get(html_key)
    if cached_html:
        return cached_html.decode("utf-8")

    # Fetch the content from the URL
    response = requests.get(url)
    html_content = response.text

    # Cache the content with a 10-second expiration
    redis_client.setex(html_key, 10, html_content)

    return html_content
