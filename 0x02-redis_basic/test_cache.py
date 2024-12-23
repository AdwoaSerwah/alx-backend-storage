#!/usr/bin/env python3
"""
Test script for Cache class.
"""

from exercise import Cache


def test_cache():
    """
    Tests the Cache class and its methods.
    """
    cache = Cache()

    TEST_CASES = {
        b"foo": None,
        123: int,
        "bar": lambda d: d.decode("utf-8")
    }

    for value, fn in TEST_CASES.items():
        key = cache.store(value)
        assert cache.get(key, fn=fn) == value

    print("All tests passed!")


if __name__ == "__main__":
    test_cache()
