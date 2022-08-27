from array import array
from random import random

# array type code 'd' means double
floats_arr = array('d', (random() for idx in range(10**7)))
print(floats_arr)