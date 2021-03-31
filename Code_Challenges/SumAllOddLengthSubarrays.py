# Given an array of positive integers arr, calculate the sum of all possible odd-length subarrays.

# A subarray is a contiguous subsequence of the array.

# Return the sum of all odd-length subarrays of arr.

# Example 1
# Input: arr = [1,4,2,5,3]
# Output: 58
# Explanation: The odd-length subarrays of arr and their sums are:
# [1] = 1
# [4] = 4
# [2] = 2
# [5] = 5
# [3] = 3
# [1,4,2] = 7
# [4,2,5] = 11
# [2,5,3] = 10
# [1,4,2,5,3] = 15
# If we add all these together we get 1 + 4 + 2 + 5 + 3 + 7 + 11 + 10 + 15 = 58

# Example 2
# Input: arr = [1,2]
# Output: 3
# Explanation: There are only 2 subarrays of odd length, [1] and [2]. Their sum is 3.

# Example 3
# Input: arr = [10,11,12]
# Output: 66
from typing import List

from rich.console import Console

from utils import timer

console = Console()


@timer
def main2(arr: List[int]) -> int:
    result = 0
    max_length = len(arr)
    if max_length % 2 == 0:
        max_length -= 1

    for i in range(1, max_length + 1, 2):
        for j in range(len(arr)):
            if j + i > len(arr):
                break
            else:
                result += sum(arr[j:j+i])
    return result


if __name__ == "__main__":
    # console.print(main2([1, 4, 2, 5, 3]))
    console.print(main2([1, 2]))
