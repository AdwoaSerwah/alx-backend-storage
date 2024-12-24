#!/usr/bin/env python3
""" Main file for testing web caching and tracking """

import redis
from web import get_page

# Redis client instance
redis_client = redis.Redis()

# Test URL with delay to simulate a slow response
url = "http://slowwly.robertomurray.co.uk/delay/5000/url/http://www.example.com"

# First call: Fetch and cache
print("Fetching content...")
print(get_page(url))  # Should fetch the content and cache it

# Second call: Fetch from cache
print("\nFetching cached content...")
print(get_page(url))  # Should retrieve content from the cache

# Verify the count
count_key = f"count:{url}"
count = redis_client.get(count_key)
print(f"\nURL accessed count: {int(count)}")  # Print the count as an integer
