# -*- coding: utf-8 -*-

from googleapi.search import query

'''
    plagiarism_check.py

    Check a sentence in the essay for plagiarism
'''

# Don't worry about these 2 lines
from essays.en1 import essay_en1
from essays.en2 import essay_en2


def split_sentences(text):
    """Change punctuation at ends of sentences all to periods and split"""
    return [sentence.lstrip() for sentence in text.replace('!', '.').replace('?', '.').replace('\n', '.').split('.')]


def check_text(text):
    """ Search the google api for hits on sentences in text """
    print('\n\nChecking for plagiarism...')
    sentences = split_sentences(text)
    length_dict = {}
    max_length = 0
    # Only check the longest sentence because the google api only allows 100 queries per day
    for sentence in sentences:
        words = sentence.split(' ')
        size = len(words)
        if size > max_length:
            max_length = size
        length_dict[size] = sentence
    check_sentence = length_dict[max_length]  # There's a more efficient way to do this without a dictionary
    num_hits = query(check_sentence)
    print('Found {} sites with this sentence\nSentence searched:\n{}'.format(num_hits, check_sentence))
    if num_hits > 0:
        print('This text is NOT original!!!')
    else:
        print('No trace of plagiarism.')


dr_seuss_quote = "You have brains in your head. You have feet in your shoes. " \
                 "You can steer yourself any direction you choose."
check_text(essay_en1)
check_text(dr_seuss_quote)
