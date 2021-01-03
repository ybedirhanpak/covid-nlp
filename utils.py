import string
from string import punctuation
import os
import pickle
import re

ALPHABET = "abcdefghijklmnopqrstuvwxyz0123456789"

stopwords = []


def get_file_path(file_name: str):
    return os.path.join(os.path.dirname(__file__), file_name)


# Read stopwords list from file
with open(get_file_path("data/stopwords.txt")) as f:
    stopwords = f.read().splitlines()
    f.close()


def is_stopword(token: str):
    '''
        Returns True if token is stopword or empty string
    '''
    return token in stopwords or token == ''


def normalize_doc(doc: str):
    '''
        Replaces punctuation characters with space character
    '''
    # NOTE FOR FUTURE ENHANCEMENTS:
    # We can use more effective punctuation removal mechanism.
    # We can make adjactives separated and word-number pairs to be concatenated.
    # For example 'non-immunocompromised' -> 'non immunocompromised'; 'covid-19' -> 'covid19'
    # We should also treat decimal numbers differently. Right now '(82.5%)' becomes 825 but it should be still '82.5' or '82.5%'
    return re.sub(f'[^{ALPHABET}]', ' ', doc.lower()).strip()


def normalize_token(token: str):
    '''
        Normalizes given token by removing trailing spaces 
    '''
    return token.strip()


def pickle_object(object, location):
    with open(get_file_path(location), 'wb') as file:
        pickle.dump(object, file, protocol=pickle.HIGHEST_PROTOCOL)


def unpickle_object(location):
    with open(get_file_path(location), 'rb') as file:
        obj = pickle.load(file)
    return obj
