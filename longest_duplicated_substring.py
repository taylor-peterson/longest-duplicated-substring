#!/usr/bin/env python3
"""Sample solutions to the longest duplicated substring problem."""


def brute_force_optimal(string):
    """Return the longest duplicated substring.

    Keyword Arguments:
    string -- the string to examine for duplicated substrings

    This approach examines each possible pair of starting points
    for duplicated substrings. If the characters at those points are
    the same, the match is extended up to the maximum length for those
    points. Each new longest duplicated substring is recorded as the
    best found so far.

    This solution is optimal for the naive brute-force approach and
    runs in O(n^3).
    """
    lds = ""
    string_length = len(string)
    for i in range(string_length):
        for j in range(i+1, string_length):
            for substring_length in range(string_length-j):
                if string[i+substring_length] != string[j+substring_length]:
                    break
                if substring_length + 1 > len(lds):
                    lds = string[i:i+substring_length+1]
    return lds
