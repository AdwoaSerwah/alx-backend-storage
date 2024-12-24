#!/usr/bin/env python3
"""
Web caching and URL tracking module.
"""

import redis
import requests
from typing import Callable

redis_client = redis.Redis()


def get_page(url: str) -> str:
    """
    Fetches the HTML content of a URL and caches it in Redis.
    Tracks the number of times the URL has been accessed.

    Args:
        url (str): The URL to fetch.

    Returns:
        str: The HTML content of the URL.
    """
    # Define keys for tracking and caching
    count_key = f"count:{url}"
    html_key = f"html:{url}"

    # Increment the URL access count
    redis_client.incr(count_key)

    # Check if the HTML content is already cached
    cached_html = redis_client.get(html_key)
    if cached_html:
        return cached_html.decode("utf-8")

    # Fetch HTML content and cache it with expiration
    response = requests.get(url)
    html_content = response.text
    redis_client.setex(html_key, 10, html_content)  # Cache for 10 seconds

    return html_content
