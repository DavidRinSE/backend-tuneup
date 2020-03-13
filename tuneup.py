#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tuneup assignment"""

__author__ = "???"

import cProfile
import pstats
import timeit


def profile(func):
    def profiled_func(args):
        profile = cProfile.Profile()
        try:
            profile.enable()
            result = func(args)
            profile.disable()
            return result
        finally:
            ps = pstats.Stats(profile).sort_stats('cumulative')
            ps.print_stats()
    return profiled_func


def read_movies(src):
    """Returns a list of movie titles"""
    print('Reading file: {}'.format(src))
    with open(src, 'r') as f:
        return f.read().splitlines()


def is_duplicate(title, movies):
    """returns True if title is within movies list"""
    # for movie in movies:
    #     if movie.lower() == title.lower():
    #         return True
    # return False
    return True if title in movies else False


@profile
def find_duplicate_movies(src):
    """Returns a list of duplicate movies from a src list"""
    movies = read_movies(src)
    duplicates = []
    while movies:
        movie = movies.pop()
        if is_duplicate(movie, movies):
            duplicates.append(movie)
    return duplicates


def timeit_helper():
    """Part A:  Obtain some profiling measurements using timeit"""
    t = timeit.Timer("main()", "print('Running main')")
    result = t.repeat(repeat=7, number=3)
    average = [res / 3 for res in result]
    print("Result: {}".format(result))
    print("Averages: {}".format(average))
    print("Min: {}".format(min(average)))


def main():
    """Computes a list of duplicate movie entries"""
    result = find_duplicate_movies('movies.txt')
    print('Found {} duplicate movies:'.format(len(result)))
    print('\n'.join(result))


if __name__ == '__main__':
    main()
