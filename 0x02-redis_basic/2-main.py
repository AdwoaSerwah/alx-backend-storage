#!/usr/bin/env python3
""" Main file """

Cache = __import__('exercise').Cache

cache = Cache()

# Call the store method three times
cache.store(b"first")
print(cache.get(f"Cache.{cache.store.__qualname__}"))  # Correct key format

cache.store(b"second")
cache.store(b"third")
print(cache.get(f"Cache.{cache.store.__qualname__}"))  # Correct key format
