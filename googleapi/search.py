# -*- coding: utf-8 -*-

"""
Using Google API to query for a sentence exact match

https://developers.google.com/custom-search/json-api/v1/overview
https://cse.google.com/cse/create/getcode?cx=016969227690395280118%3Aej0xpwldlgc

"""

import requests
import json
import urllib

API_KEY = 'AIzaSyDf0vgrDWiZ12wTtpl2RWZzmRbNGEyOzuY'
ENGINE = '016969227690395280118:ej0xpwldlgc'


def add_quotes(query):
    """If search string is not quoted, quote it"""
    if not query.startswith('"'):
        query = '"{}"'.format(query)
    return query


def query(query):
    """ Query google api """
    query = add_quotes(query)
    # query = urllib.quote_plus(query) # Python 2
    query = urllib.parse.quote_plus(query)  # Python 3
    request = 'https://www.googleapis.com/customsearch/v1?key={}&cx={}&q={}'.format(API_KEY, ENGINE, query)
    response = json.loads(requests.get(request).text)
    total_results = int(response['searchInformation']['totalResults'])
    return total_results
