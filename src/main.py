from lang import *
from util import numeral_list, print_numeral_list


lst = numeral_list([2, 5, 1, 9, 3, 7, 4, 6, 8])
test = RANGE(ONE)(NUMBER(10))

# lambda calculus merge sort
ms = lambda arr: IF_THEN_ELSE(LT(LENGTH(arr))(NUMBER(2)))(arr)(MERGE(ms(TAKE(DIV(LENGTH(arr))(NUMBER(2)))(arr)))(ms(DROP(DIV(LENGTH(arr))(NUMBER(2)))(arr))))

print("Test:")
print_numeral_list(test)
print("Sorted:")
print_numeral_list(ms(lst))
