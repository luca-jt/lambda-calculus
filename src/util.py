from lang import IS_EMPTY, TAIL, TRUE, HEAD, to_numeral, LIST, APPEND


def decode_numeral(numeral) -> int:
    return numeral(lambda i: i + 1)(0)

def print_numeral(numeral):
    print(decode_numeral(numeral))

def numeral_list(py_list: list[int]):
    lst = LIST
    for num in py_list:
        lst = APPEND(to_numeral(num))(lst)
    return lst

def print_numeral_list(c_list):
    py_list = []
    while True:
        if IS_EMPTY(c_list) is TRUE:
            break
        py_list.append(decode_numeral(HEAD(c_list)))
        c_list = TAIL(c_list)
    print(py_list)
