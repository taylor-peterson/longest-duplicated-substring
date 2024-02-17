[![Python application](https://github.com/taylor-peterson/longest-duplicated-substring/actions/workflows/python-app.yml/badge.svg)](https://github.com/taylor-peterson/longest-duplicated-substring/actions/workflows/python-app.yml)

# Overview
This problem appears in [Programming Pearls](http://www.amazon.com/Programming-Pearls-2nd-Jon-Bentley/dp/0201657880/ref=sr_1_1?ie=UTF8&s=books&qid=1268415457&sr=8-1).

The problem is quick to state, and easy to give over a phone screen.

# Problem
Given a string, return the longest duplicated substring.

## Examples
* "banana" -> "ana"
* "tomato" -> "to"
* "aaaaa" -> "aaaa"

## Solutions
There are a wide range of approaches, ranging from O(n^4) all the way down to linear time.

Many common approaches are provided in this package in Python; translating them to
other languages is a trivial exercise left to the reader.

## Runtime of Common Operations
* String comparison: O(n)
* String slice of size m: O(m)
* Substring: O(n) (note that this was O(1) prior to Java 7)
