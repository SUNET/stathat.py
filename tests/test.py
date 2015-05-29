from unittest import TestCase
from stathat import StatHat

__author__ = 'ft'


class StatHat_tests(TestCase):

    def setUp(self):
        self.stathat = StatHat('test@example.org')

    def test_parse_accept_lang_header(self):
        self.assertEqual(self.stathat.email, 'test@example.org')

