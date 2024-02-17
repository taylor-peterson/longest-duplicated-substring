"""Unit testing for the sample solutions to longest_duplicated_substring."""

import pytest

import longest_duplicated_substring


@pytest.mark.parametrize(
    ('string,result'),
    [
        pytest.param('banana', 'ana',  id="Overlapping substrings"),
        pytest.param('tomato', 'to',   id="Non-overlapping substring"),
        pytest.param('aaaaa',  'aaaa', id="Repeated character"),
        pytest.param('Goat',   '',     id="No substring"),
        pytest.param('',       '',     id="No String"),
    ],
)
def test_brute_force_optimal(string, result):
    """Run all test cases against all solutions."""
    assert longest_duplicated_substring.brute_force_naive(string) == result
    assert longest_duplicated_substring.brute_force_optimal(string) == result
