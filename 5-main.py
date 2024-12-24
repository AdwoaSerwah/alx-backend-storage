#!/usr/bin/env python3
""" Main file for testing web.py """

get_page = __import__('web').get_page

url = "http://slowwly.robertomurray.co.uk/delay/5000/url/http://www.example.com"

print(get_page(url))  # Fetches and caches the HTML content
print(get_page(url))  # Retrieves the content from the cache
