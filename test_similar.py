#-*- coding: utf-8 -*

import unittest
from similar.similar import Similar
from similar.similar import best_match
from similar.exceptions import NoResultException


class SimilarTestCase(unittest.TestCase):

    def setUp(self):
        self.haystack = [word.strip() for word in open('test_wordlist.txt')]
        self.needle = 'bananna'
        self.correct_word = 'banana'

    def test_similar_in_list(self):
        s = Similar(self.needle, self.haystack)
        self.assertEqual(s.best(), self.correct_word)

    def test_similar_in_wordlist(self):
        s = Similar(self.needle, open('test_wordlist.txt'))
        self.assertEqual(s.best(), self.correct_word)

    def test_similar_in_generator(self):
        def genwords():
            for line in open('test_wordlist.txt'):
                yield line

        s = Similar(self.needle, genwords())
        self.assertEqual(s.best(), self.correct_word)

    def test_best_match(self):
        best = best_match(self.needle, self.haystack)
        self.assertEqual(best, self.correct_word)

    def test_results(self):
        s = Similar(self.needle, self.haystack)
        self.assertEqual(len(s.results()), len(self.haystack))

    def test_no_result_exception(self):
        with self.assertRaises(NoResultException):
            s = Similar('foo', [])
            s.best()


if __name__ == '__main__':
    unittest.main()