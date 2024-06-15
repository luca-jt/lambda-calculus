from lang import *
from util import numeral_list, print_numeral_list


lst = numeral_list([2, 5, 1, 9, 3, 7, 4, 6, 8])
test = RANGE(ONE)(NUMBER(10))

# lambda calculus merge sort
len_check = lambda arr: LT(LENGTH(arr))(NUMBER(2))
half1 = lambda arr: TAKE(DIV(LENGTH(arr))(NUMBER(2)))(arr)
half2 = lambda arr: DROP(DIV(LENGTH(arr))(NUMBER(2)))(arr)
merge_sort = lambda arr: IF_THEN_ELSE(len_check(arr))(arr)(MERGE(merge_sort(half1(arr)))(merge_sort(half2(arr))))

print("Test:")
print_numeral_list(test)
print("Sorted:")
print_numeral_list(merge_sort(lst))
