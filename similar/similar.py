# -*- coding: utf-8 -*

import operator
import Levenshtein
from .exceptions import NoResultException


class Similar(object):
    """
    The main class used to search similar words.
    """

    def __init__(self, needle, haystack):
        self.needle = needle
        self.haystack = haystack

    def best(self):
        """
        Returns the best similar word.
        """
        results = self.results()
        return results[0][0]

    def results(self):
        """
        Returns a list of tuple, ordered by similarity.
        """
        d = dict()
        words = [word.strip() for word in self.haystack]

        if not words:
            raise NoResultException('No similar word found.')

        for w in words:
            d[w] = Levenshtein.ratio(self.needle, w)

        return sorted(d.items(), key=operator.itemgetter(1), reverse=True)


def best_match(needle, haystack):
    """
    Constructs a Similar object and returns the best result found.
    """
    p = Similar(needle, haystack)
    return p.best()
