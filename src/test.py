import pytest
from lang import *
from util import decode_numeral, decode_numeral_list

@pytest.mark.parametrize('low, high', [
    (ZERO, ONE),
    (TEN, NUMBER(11)),
    (NUMBER(22), NUMBER(23)),
])
def test_succ_pred(low, high):
    assert SUCC(low) is high
    assert PRED(high) is low


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


@pytest.mark.parametrize('number, nmrl', [
    (ZERO, 0),
    (FIVE, 5),
    (NUMBER(22), 22),
])
def test_decode(number, nmrl):
    assert decode_numeral(number) is nmrl


@pytest.mark.parametrize('num_list, numeral_l', [
    (numeral_list([]), []),
    (numeral_list([1]), [1]),
    (numeral_list([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5]),
])
def test_decode_list(num_list, numeral_l):
    assert decode_numeral_list(num_list) is numeral_l


@pytest.mark.parametrize('given', [
    [],
    [1],
    [1, 2],
    [1, 2, 3],
])
def test_prepend(given):
    lst = LIST
    for el in reversed(given):
        lst = INSERT_FRONT(lst)(el)
    assert decode_numeral_list(lst) == given


@pytest.mark.parametrize('given', [
    [],
    [1],
    [1, 2],
    [1, 2, 3],
])
def test_append(given):
    lst = LIST
    for el in given:
        lst = APPEND(lst)(el)
    assert decode_numeral_list(lst) == given


@pytest.mark.parametrize('given', [
    [],
    [1],
    [1, 2],
    [1, 2, 3],
])
def test_reverse(given):
    lst = LIST
    for el in given:
        lst = INSERT_FRONT(lst)(el)
    assert decode_numeral_list(REVERSE(lst)) == given


@pytest.mark.parametrize('given, expected', [
    ([], 0),
    ([ONE], 1),
    ([ONE, TWO], 3),
    ([ONE, TWO, THREE], 6),
])
def test_reduce(given, expected):
    lst = LIST
    for el in given:
        lst = INSERT_FRONT(lst)(el)
    assert decode_numeral_list(REDUCE(PLUS)(lst)(ZERO)) == expected


@pytest.mark.parametrize('given, expected', [
    ([], []),
    ([ONE], [3]),
    ([ONE, TWO, THREE], [3, 4, 5]),
])
def test_map(given, expected):
    lst = LIST
    for el in reversed(given):
        lst = INSERT_FRONT(lst)(el)
    res = MAP(PLUS(TWO))(lst)
    decoded = [decode_numeral(num) for num in decode_numeral_list(res)]
    assert decoded == expected


@pytest.mark.parametrize('start, end, expected', [
    (ONE, ONE, []),
    (THREE, ONE, []),
    (ONE, THREE, [1, 2]),
])
def test_range(start, end, expected):
    res = RANGE(start)(end)
    decoded = [decode_numeral(num) for num in decode_numeral_list(res)]
    assert decoded == expected


@pytest.mark.parametrize('given, expected', [
    ([ONE], []),
    ([ONE, ONE], []),
    ([FOUR], [4]),
    ([ONE, TWO], [2]),
    ([THREE, ONE, TWO], [3, 2]),
])
def test_filter(given, expected):
    lst = LIST
    for el in given:
        lst = APPEND(lst)(el)
    res = FILTER(LTE(TWO))(lst)
    decoded = [decode_numeral(num) for num in decode_numeral_list(res)]
    assert decoded == expected


@pytest.mark.parametrize('given, number, expected', [
    ([1, 2, 3], ONE, [2, 3]),
])
def test_drop(given, number, expected):
    lst = LIST
    for el in given:
        lst = APPEND(lst)(el)
    res = DROP(number)(lst)
    assert decode_numeral_list(res) == expected


@pytest.mark.parametrize('given, number, expected', [
    ([1, 2, 3], TWO, [1, 2]),
    ([1, 2, 3], FOUR, [1, 2, 3]),
    ([1, 2, 3], ZERO, []),
    ([], TWO, []),
])
def test_take(given, number, expected):
    lst = LIST
    for el in given:
        lst = APPEND(lst)(el)
    res = TAKE(number)(lst)
    assert decode_numeral_list(res) == expected


@pytest.mark.parametrize('given, expected', [
    ([], 0),
    ([4], 1),
    ([4, 5], 2),
    ([1, 2, 3], 3),
])
def test_length(given, expected):
    lst = LIST
    for el in given:
        lst = APPEND(lst)(el)
    assert decode_numeral_list(LENGTH(lst)) == expected


@pytest.mark.parametrize('given, number, expected', [
    ([1, 2, 3], ONE, 2),
])
def test_index(given, number, expected):
    lst = LIST
    for el in given:
        lst = APPEND(lst)(el)
    res = INDEX(number)(lst)
    if expected is not None:
        assert res == expected
