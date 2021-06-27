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


def soln2(nums: List[int], k: int) -> int:
    def horace_quick_select(nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        starter_idx = len(nums) - 1
        swap_idx = 0
        scan_idx = 0
        while scan_idx < starter_idx:
            if nums[scan_idx] > nums[starter_idx]:
                scan_idx += 1
            else:
                nums[swap_idx], nums[scan_idx] = nums[scan_idx], nums[swap_idx]
                swap_idx += 1
                scan_idx += 1
        nums[swap_idx], nums[starter_idx] = nums[starter_idx], nums[swap_idx]
        left = horace_quick_select(nums[:swap_idx])
        right = horace_quick_select(nums[swap_idx+1:])
        return left + [nums[swap_idx]] + right
    return horace_quick_select(nums)[-k]


print(soln2(nums1, k1))
print(soln2(nums2, k2))
