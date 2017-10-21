# -*- coding: utf-8 -*-

"""
Using Google API to query for a sentence exact match

https://developers.google.com/custom-search/json-api/v1/overview
https://cse.google.com/cse/create/getcode?cx=016969227690395280118%3Aej0xpwldlgc

"""

import requests
import json
import urllib
import os

API_KEY = os.getenv('API_KEY', None)
ENGINE = '016969227690395280118:ej0xpwldlgc'


def add_quotes(query):
    """If search string is not quoted, quote it"""
    if not query.startswith('"'):
        query = '"{}"'.format(query)
    return query


def query(query):
    """ Query google api """
    if not API_KEY:
        raise ValueError('API_KEY is not set.  Type:\nexport API_KEY=YOURKEY\n\nGet an API key here! '
                         'https://developers.google.com/custom-search/json-api/v1/overview')
    query = add_quotes(query)
    # query = urllib.quote_plus(query) # Python 2
    query = urllib.parse.quote_plus(query)  # Python 3
    request = 'https://www.googleapis.com/customsearch/v1?key={}&cx={}&q={}'.format(API_KEY, ENGINE, query)
    response = json.loads(requests.get(request).text)
    total_results = int(response['searchInformation']['totalResults'])
    return total_results
