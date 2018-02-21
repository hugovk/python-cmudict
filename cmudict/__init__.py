# -*- coding: utf-8 -*-

"""
This module provides access to the location and stream of the cmudict files.
The default function where() returns the location of the cmudict.dict file.
"""

import re
from collections import defaultdict

import pkg_resources

__version__ = pkg_resources.resource_string(
    'cmudict', 'VERSION').decode('utf-8').strip()


def _stream(resource_name):
    stream = pkg_resources.resource_stream(__name__, resource_name)
    return stream


def _string(resource_name):
    string = pkg_resources.resource_string(__name__, resource_name)
    return string


def _entries(stream):
    entries = []
    for line in stream:
        parts = line.decode('utf-8').strip().split()
        thing = re.sub(r'\(\d+\)$', '', parts[0])
        entries.append((thing, parts[1:]))
    return entries


def dict():
    """
    Compatibility with NLTK.
    Returns the cmudict lexicon as a dictionary, whose keys are
    lowercase words and whose values are lists of pronunciations.
    """
    default = defaultdict(list)
    for key, value in entries():
        default[key].append(value)
    return default


def dict_stream():
    """Return a readable file-like object of the cmudict.dict file."""
    stream = _stream('data/cmudict.dict')
    return stream


def dict_string():
    """Return the contents of cmudict.dict as a string."""
    string = _string('data/cmudict.dict')
    return string


def license_string():
    """Return the contents of LICENSE as a string."""
    string = _string('data/LICENSE')
    return string


def phones():
    phones = []
    for line in phones_stream():
        parts = line.decode('utf-8').strip().split()
        phones.append((parts[0], parts[1:]))
    return phones


def phones_stream():
    """Return a readable file-like object of the cmudict.phones file."""
    s = _stream('data/cmudict.phones')
    return s


def phones_string():
    """Return the contents of cmudict.phones as a string."""
    string = _string('data/cmudict.phones')
    return string


def symbols():
    symbols = []
    for line in symbols_stream():
        symbols.append(line.decode('utf-8').strip())
    return symbols


def symbols_stream():
    """Return a readable file-like object of the cmudict.symbols file."""
    stream = _stream('data/cmudict.symbols')
    return stream


def symbols_string():
    """Return the contents of cmudict.symbols as a string."""
    string = _string('data/cmudict.symbols')
    return string


def vp():
    vp = defaultdict(list)
    for key, value in _entries(vp_stream()):
        vp[key].append(value)
    return vp


def vp_stream():
    """Return a readable file-like object of the cmudict.vp file."""
    stream = _stream('data/cmudict.vp')
    return stream


def vp_string():
    """Return the contents of cmudict.vp as a string."""
    string = _stream('data/cmudict.vp')
    return string


# The entries(), raw(), and words() maintain compatability with NTLK
def entries():
    """
    Compatibility with NLTK.
    Returns the cmudict lexicon as a list of entries
    containing (word, transcriptions) tuples.
    """
    entries = []
    for line in dict_stream():
        parts = line.decode('utf-8').strip().split()
        word = re.sub(r'\(\d+\)$', '', parts[0])
        entries.append((word, parts[1:]))
    return entries


def raw():
    """
    Compatibility with NLTK.
    Returns the cmudict lexicon as a raw string.
    """
    string = pkg_resources.resource_string(__name__, 'data/cmudict.dict')
    return string.decode('utf-8')


def words():
    """
    Compatibility with NLTK.
    Returns a list of all words defined in the cmudict lexicon.
    """
    return [word.lower() for (word, _) in entries()]
