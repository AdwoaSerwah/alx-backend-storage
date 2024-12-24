#!/usr/bin/env python3
"""Web Cache and Tracker using Redis."""


import requests
import redis


def connect_to_redis(host='localhost', port=6379, db=0):
    """Connect to the Redis server.

    Parameters:
    host (str): The host where Redis is running. Default is 'localhost'.
    port (int): The port number. Default is 6379.
    db (int): The database number. Default is 0.

    Returns:
    redis.Redis: A Redis client object.
    """
    return redis.Redis(host=host, port=port, db=db)


# Connect to Redis at the module level
redis_client = connect_to_redis()


def get_page(url: str) -> str:
    """Fetch the HTML content of the specified URL, cache it, and track
    access counts.

    Parameters:
    url (str): The URL to fetch.

    Returns:
    str: The HTML content of the URL.
    """
    # Increase the count for this URL
    count_key = f"count:{url}"
    redis_client.incr(count_key)

    # Check if the page is cached
    cache_key = f"cache:{url}"
    cached_page = redis_client.get(cache_key)
    if cached_page:
        return cached_page.decode('utf-8')

    # Fetch the page from the internet
    response = requests.get(url)
    response.raise_for_status()  # Ensure the request was successful
    content = response.text

    # Cache the response with an expiration of 10 seconds
    redis_client.setex(cache_key, 10, content)

    return content


def main():
    """Main function to test get_page."""
    u = "http://slowwly.robertomurray.co.uk/delay/2000/url/http://example.com"
    print(get_page(u))  # This will take time due to the delay
    print(get_page(u))  # This will be instant because it's cached
    print(redis_client.get(f"count:{u}").decode('utf-8'))


if __name__ == "__main__":
    main()
