# Task
# Given an integer,

# , perform the following conditional actions:

#     If

# is odd, print Weird
# If
# is even and in the inclusive range of to
# , print Not Weird
# If
# is even and in the inclusive range of to
# , print Weird
# If
# is even and greater than

#     , print Not Weird

# Input Format

# A single line containing a positive integer,

# .

# Constraints

# Output Format

# Print Weird if the number is weird. Otherwise, print Not Weird.

import math
import os
import random
import re
import sys


if __name__ == "__main__":
    n = int(input().strip())

    is_even = n % 2 == 0
    is_even_greater_than_20 = is_even and n > 20
    is_even_between_6_and_20 = is_even and n >= 6 and n <= 20

    if not is_even:
        print("Weird")
    elif is_even_greater_than_20:
        print("Not Weird")
    elif is_even_between_6_and_20:
        print("Weird")
    else:
        print("Not Weird")
