import unittest
import argparse
from movie.main import main
from sqlite3_db.create_db import movies
from movie.movie_library import MovieLibrary
from unittest import TestCase
from unittest.mock import patch, Mock

class Main_test(unittest.TestCase):

    def test_movlst(self):
        self.assertEqual(True, False)

    def test_movdt(self):
        self.assertEqual(True, False)

    def test_movsrch(self):
        self.assertEqual(True, False)

    def test_movadd(self):
        self.assertEqual(True, False)

    def test_movrmv(self):
        self.assertEqual(True, False)

    def test_movfv(self):
        self.assertEqual(True, False)

    def test_movcat(self):
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()


def test_mock_args(mocker, movie):
    mocker.patch('argparse.ArgumentParser.parse_args',
                return_value=argparse.Namespace(args='mocked'))
    assert 'mocked' == movie.movie.main.get_args()


class MockArgs:
    def __init__(self, args):
        self.args = args

    def get_args(self):
        return self.args


class TestCommandLine(TestCase):

    def setUp(self, module_name=main):
        """Method called to prepare the test fixture. This is called immediately before calling the test method"""
        self.parser = module_name()

    def test_no_arguments(self):
        opts = self.parser.parse_arguments([])
        assert opts.fs_name

    def tearDown(self):
        """Method called immediately after the test method has been called and the result recorded"""
        pass
