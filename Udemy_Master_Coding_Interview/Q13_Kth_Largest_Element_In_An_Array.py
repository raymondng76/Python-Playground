# 215
# Given an int array and an int k, return the kth largest element in the array.

from typing import List


def soln(nums: List[int], k: int) -> int:
    return sorted(nums)[-k]


nums1 = [3, 2, 1, 5, 6, 4]
k1 = 2  # 5
nums2 = [3, 2, 3, 1, 2, 4, 5, 5, 6]
k2 = 4  # 4

print(soln(nums1, k1))
print(soln(nums2, k2))
