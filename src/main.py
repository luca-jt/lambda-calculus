from lang import *
from util import print_numeral_list, print_numeral


lst = numeral_list([1, 0])
test = RANGE(ZERO)(TWO)

def merge_sort(arr):
    if LT(LENGTH(arr))(TWO) is TRUE:
        return arr
    left = merge_sort(SPLIT1(arr))
    right = merge_sort(SPLIT2(arr))
    merged = MERGE(left)(right)
    return merged

print("Sum:")
print_numeral(SUM(lst))
print("Test:")
print_numeral_list(test)
print("Index removed:")
print_numeral_list(RM_IDX(test)(TWO))
print("Sorted:")
print_numeral_list(merge_sort(lst))
