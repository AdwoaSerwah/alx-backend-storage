import redis
import requests
from typing import Callable
from functools import wraps

# Create Redis client
r = redis.Redis()


def count_calls(method: Callable) -> Callable:
    """ Decorator that counts the number of times a method is called """
    @wraps(method)
    def wrapper(*args, **kwargs):
        # Use method qualified name for the count key
        count_key = f"count:{method.__qualname__}"
        # Increment the count in Redis
        r.incr(count_key)
        return method(*args, **kwargs)
    return wrapper


@count_calls
def get_page(url: str) -> str:
    """
    Fetch the HTML content of a page from the URL and caches it for 10 seconds.

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
