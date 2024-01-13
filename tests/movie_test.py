import unittest
from collections import namedtuple
from unittest import TestCase
from movie.movie import Movie

class Movie_test(TestCase):
    args_tuple = namedtuple('args', 'arg1 arg2 arg3 arg4 arg5 args6 args7 args8')

    def test_arg1(self):
        args = Movie.args_tuple(None, 5500, None, None, None)
        res = Movie.main(args)
        assert res == [args.name], 'arg1 failed'

    def test_arg2(self):
        args = Movie.args_tuple(None, None, "Cats", None, None)
        res = Movie.main(args)
        assert res == [args.release_date], 'arg2 failed'

    def test_arg3(self):
        args = Movie.args_tuple(None, None, None, "Tom Hooper", None)
        res = Movie.main(args)
        assert res == [args.director], 'arg3 failed'

    def test_arg4(self):
        args = Movie.args_tuple(None, None, None, None, "Comedy")
        res = Movie.main(args)
        assert res == [args.genre], 'arg4 failed'

    def test_arg5(self):
        args = Movie.args_tuple(None, None, None, None, None)
        res = Movie.main(args)
        assert res == [args.user_likes], 'arg5 failed'

    def test_arg6(self):
        args = Movie.args_tuple(None, None, None, None, None)
        res = Movie.main(args)
        assert res == [args.category], 'arg6 failed'

    def test_arg7(self):
        args = Movie.args_tuple(None, None, None, None, None)
        res = Movie.main(args)
        assert res == [args.query], 'arg7 failed'

    def test_arg8(self):
        args = Movie.args_tuple(None, None, None, None, None)
        res = Movie.main(args)
        assert res == [args.movie_id], 'arg8 failed'


if __name__ == '__main__':
    unittest.main()
