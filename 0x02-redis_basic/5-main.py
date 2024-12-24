#!/usr/bin/env python3
"""
Script to verify the caching and access count behavior of the get_page function.
"""

import time
from web import get_page
import redis

# Create Redis client
r = redis.Redis()

def check_cache_and_count(url: str):
    """ Function to check if the cache is working and count is tracked correctly """
    # Check the initial count and cache
    count_key = f"count:{get_page.__qualname__}"
    initial_count = r.get(count_key)  # Get the current access count from Redis

    print(f"Initial count for {url}: {initial_count if initial_count else 0}")

    # Get the page for the first time
    print("\nFetching content for the first time...")
    get_page(url)

    # Get the count after first access
    count_after_first = r.get(count_key)
    print(f"Count after first access: {count_after_first if count_after_first else 0}")

    # Wait for 5 seconds and fetch the page again to verify cache behavior
    time.sleep(5)
    print("\nFetching content after 5 seconds...")
    get_page(url)

    # Get the count after second access
    count_after_second = r.get(count_key)
    print(f"Count after second access: {count_after_second if count_after_second else 0}")

    # Wait for 6 more seconds to ensure cache expiration
    time.sleep(6)
    print("\nWaiting for cache to expire (after 10 seconds)...")

    # Check if the cache is expired and if the count is still available
    expired_content = r.get(url)
    print(f"Cache expired after 10 seconds: {'Cache is not available' if not expired_content else 'Cache is still available'}")

    final_count = r.get(count_key)
    print(f"Final count for {url}: {final_count if final_count else 0}")

if __name__ == "__main__":
    url = "http://google.com"
    check_cache_and_count(url)
