import pytest
from lang import *
from util import decode_numeral, decode_numeral_list

@pytest.mark.parametrize('low, high', [
    (ZERO, ONE),
    (TEN, NUMBER(11)),
    (NUMBER(22), NUMBER(23)),
])
def test_succ_pred_decode(low, high):
    assert decode_numeral(SUCC(low)) == decode_numeral(high)
    assert decode_numeral(PRED(high)) == decode_numeral(low)


@pytest.mark.parametrize('left, right, expected', [
    (FALSE, FALSE, FALSE),
    (FALSE, TRUE, FALSE),
    (TRUE, FALSE, FALSE),
    (TRUE, TRUE, TRUE),
])
def test_and(left, right, expected):
    assert AND(left)(right) is expected


@pytest.mark.parametrize('left, right, expected', [
    (FALSE, FALSE, FALSE),
    (FALSE, TRUE, TRUE),
    (TRUE, FALSE, TRUE),
    (TRUE, TRUE, TRUE),
])
def test_or(left, right, expected):
    assert OR(left)(right) is expected


@pytest.mark.parametrize('given, expected', [
    (FALSE, TRUE),
    (TRUE, FALSE),
])
def test_not(given, expected):
    assert NOT(given) is expected


@pytest.mark.parametrize('left, right, expected', [
    (FALSE, FALSE, FALSE),
    (FALSE, TRUE, TRUE),
    (TRUE, FALSE, TRUE),
    (TRUE, TRUE, FALSE),
])
def test_xor(left, right, expected):
    assert XOR(left)(right) is expected


@pytest.mark.parametrize('inp, expected', [
    (TRUE, ONE),
    (FALSE, ZERO),
])
def test_bool_to_int(inp, expected):
    assert BOOL_TO_INT(inp) is expected


@pytest.mark.parametrize('inp, expected', [
    (ZERO, FALSE),
    (ONE, TRUE),
    (FIVE, TRUE),
])
def test_int_to_bool(inp, expected):
    assert INT_TO_BOOL(inp) is expected


@pytest.mark.parametrize('num_list, numeral_l', [
    (numeral_list([]), []),
    (numeral_list([1]), [1]),
    (numeral_list([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5]),
])
def test_decode_list(num_list, numeral_l):
    assert decode_numeral_list(num_list) == numeral_l
