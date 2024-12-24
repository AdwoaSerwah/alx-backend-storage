#!/usr/bin/env python3
""" Main file to verify caching and count increments for get_page """

from web import get_page
import redis
import time

# Redis client
redis_client = redis.Redis()

# Test URL
url = "http://google.com"

# Step 1: Check if the URL is already cached
cached_content = redis_client.get(url)
if cached_content:
    print(f"Cached content found: {cached_content.decode('utf-8')}")
else:
    print(f"No cached content for {url}")

# Step 2: Fetch the page for the first time
print("\nFetching content for the first time...")
get_page(url)  # First access

# Ensure the count key exists, if not initialize it
count_key = f"count:{url}"
count_after_first = redis_client.get(count_key)
if not count_after_first:
    count_after_first = 0
else:
    count_after_first = int(count_after_first)

# Step 3: Check count after first access
print(f"Count after first access: {count_after_first}")

# Step 4: Wait for 5 seconds (before the cache expires)
print("\nWaiting for 5 seconds...")
time.sleep(5)

# Step 5: Check cached content again (before it expires)
cached_content_5s = redis_client.get(url)
if cached_content_5s:
    print(f"Content after 5 seconds (still cached): yes still cached")
else:
    print(f"Content after 5 seconds: No cache available")

# Step 6: Fetch the page for the second time (to refresh cache)
print("\nFetching content for the second time...")
get_page(url)  # Second access

# Step 7: Check count after second access
count_after_second = redis_client.get(count_key)
if not count_after_second:
    count_after_second = 0
else:
    count_after_second = int(count_after_second)
print(f"Count after second access: {count_after_second}")

# Step 8: Wait for 6 more seconds (total 11 seconds) to ensure cache expires
print("\nWaiting for 6 more seconds to allow cache expiration...")
time.sleep(6)

# Step 9: Check if the cache has expired (after 11 seconds)
cached_content_expired = redis_client.get(url)
if cached_content_expired:
    print(f"Cache expired after 11 seconds: Still cached - yes")
else:
    print(f"Cache expired after 11 seconds: Cache is not available")

# Step 10: Check the final count after all accesses
final_count = redis_client.get(count_key)
if not final_count:
    final_count = 0
else:
    final_count = int(final_count)
print(f"Final count for {url}: {final_count}")
