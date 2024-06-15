from lang import RANGE, ONE, NUMBER, LIST
from util import numeral_list, print_numeral_list


lst = numeral_list([2, 5, 1, 9, 3, 7, 4, 6, 8])
test = RANGE(ONE)(NUMBER(10))

# merge sort
sort = LIST

print_numeral_list(test)
print_numeral_list(sort)
