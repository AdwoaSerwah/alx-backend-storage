#!/usr/bin/env python3
""" Main file for testing web caching and tracking """

import time
from web import get_page
import redis

# Redis client
redis_client = redis.Redis()

# Test URL
url = "http://google.com"

# First call: Fetch and cache
print("Fetching content...")
print(get_page(url))

# Check count after first call
count_key = f"count:{url}"
print(f"\nURL accessed count after first call: {int(redis_client.get(count_key))}")

# Wait 5 seconds and call again (should fetch from cache)
time.sleep(5)
print("\nFetching cached content...")
print(get_page(url))
print(f"URL accessed count after second call: {int(redis_client.get(count_key))}")

# Wait another 6 seconds (cache should expire) and call again
time.sleep(6)
print("\nFetching content after cache expiry...")
print(get_page(url))
print(f"URL accessed count after third call: {int(redis_client.get(count_key))}")
