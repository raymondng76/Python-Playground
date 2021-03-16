# Given an array of intergers, arr, and three integers a, b, and c. You need to find the number of good triplets.
# A triplets (arr[i], arr[j], arr[k]) is good if the following condition is true.
# 0 <= i < j < k < arr.length
# |arr[i] - arr[j]| <= a
# |arr[j] - arr[k]| <= b
# |arr[i] - arr[k]| <= c

# Example 1:
# Input: arr = [3,0,1,1,9,7], a = 7, b = 2, c = 3
# Output: 4
# Explanation: There are 4 good triplets: [(3,0,1), (3,0,1), (3,1,1), (0,1,1)].

# Example 2:
# Input: arr = [1,1,2,2,3], a = 0, b = 0, c = 1
# Output: 0
# Explanation: No triplet satisfies all conditions.
from typing import List

from rich.console import Console

console = Console()


def main(arr: List[int], a: int, b: int, c: int) -> int:
    result = []
    for i in range(len(arr) - 2):
        for j in range(len(arr[i:])):
            for k in range(len(arr[j:])):
                j = i + 1
                k = i + 2
                cond1 = abs(arr[i] - arr[j]) <= a
                cond2 = abs(arr[j] - arr[k]) <= b
                cond3 = abs(arr[i] - arr[k]) <= c
                if cond1 and cond2 and cond3:
                    result.append((arr[i], arr[j], arr[k]))
    console.print(set(result))
    return len(result)


if __name__ == "__main__":
    console.print(main([3, 0, 1, 1, 9, 7], a=7, b=2, c=3))
    # console.print(main([1, 1, 2, 2, 3], a=0, b=0, c=1))
    # WIP
