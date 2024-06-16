from lang import *
from util import print_numeral_list, print_numeral


test = RANGE(ZERO)(TEN)

print("Test:")
print_numeral_list(test)
print("Sum:")
print_numeral(SUM(test))
