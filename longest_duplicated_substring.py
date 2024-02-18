#!/usr/bin/env python3
"""Sample solutions to the longest duplicated substring problem."""


def brute_force_naive(string):
    """Generate all substrings, compare each for equality, and keep the longest.

    Ends up being O(n^5)!
    """
    n = len(string)

    substrings = []
    for i in range(n):
        for j in range(i, n):
            substrings.append(string[i:j+1])

    lds = ""
    for i, a in enumerate(substrings):
        for b in substrings[i+1:]:
            if a == b and len(a) > len(lds):
                lds = a

    return lds


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


def brute_force_hash(string):
    """Generate all substrings, hash each, log the longest duplicate. O(n^3)"""
    lds = ""
    seen = set()

    n = len(string)
    for i in range(n):
        for j in range(i+1, n):
            ss = string[i:j+1]
            print(ss)
            if ss in seen and len(ss) > len(lds):
                lds = ss
            else:
                seen.add(ss)

    return lds


def binary_search(string):
    """
    Instead of looking at substrings of all possible lengths,
    halve the search space at each go.

    Note that if there is a duplicated substring of length 10,
    there's also one of length 9,8,7...
    """
    n = len(string)
    left = 0
    right = n - 1  # max possible duplicated substring length

    lds = ""
    while left <= right:
        m = (left + right) // 2
        seen = set()
        for i in range(n-m+1):
            ss = string[i:i+m]
            if ss in seen:
                lds = ss
                break
            else:
                seen.add(ss)
        if len(lds) == m:
            left = m+1
        else:
            right = m-1

    return lds
