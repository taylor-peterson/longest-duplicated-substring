import pytest

from longest_duplicated_substring import *


def pytest_generate_tests(metafunc):
     """
     If a test function has a idparametrize mark, use it to create parametrized
     tests with ids. To use, provide a tuple of argnames and a dictionary of
     test id strings -> tuples of test values. For example:
         @py.test.mark.idparametrize(('a', 'b'), {
             'foo': (1, 2),
             'bar': (3, 4),})
     Note tests will be ordered alphabetically by test id string.
     """
     idparametrize = getattr(metafunc.function, 'idparametrize', None)
     if idparametrize:
         argnames, testdata = idparametrize.args
         ids, argvalues = zip(*sorted(testdata.items()))
         metafunc.parametrize(argnames, argvalues, ids=ids)

scenarios = pytest.mark.idparametrize  # Convenience variable.


@scenarios(('string', 'result'), {
    'Overlapping substrings': ('banana', 'ana'),
    'Non-overlapping substring': ('tomato', 'to'),
    'Repeated character': ('aaaaa', 'aaaa'),
    'No substring': ('Goat', ''),
    'No string': ('', ''),
})
def test_brute_force_optimal(string, result):
    assert brute_force_optimal(string) == result
