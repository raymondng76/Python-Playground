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
    def quick_sort(nums: List[int]) -> List[int]:
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
        return quick_sort(nums[:swap_idx]) + [nums[swap_idx]] + quick_sort(nums[swap_idx+1:])
    return quick_sort(nums)[-k]


print(soln2(nums1, k1))
print(soln2(nums2, k2))


def soln3(nums: List[int], k: int) -> int:
    def partition(nums: List[int], left: int, right: int) -> List[int]:
        pivot = nums[right]
        partition_idx = left - 1
        for idx in range(left, right):
            if nums[idx] <= pivot:
                partition_idx += 1
                nums[partition_idx], nums[idx] = nums[idx], nums[partition_idx]
        nums[partition_idx + 1], nums[right] = nums[right], nums[partition_idx + 1]
        return partition_idx + 1

    def quick_sort(nums: List[int], left: int, right: int) -> List[int]:
        if len(nums) == 1:
            return nums
        if left < right:
            partition_idx = partition(nums, left, right)
            quick_sort(nums, left, partition_idx - 1)
            quick_sort(nums, partition_idx + 1, right)
    quick_sort(nums, 0, len(nums) - 1)
    return nums[-k]


print(soln3(nums1, k1))
print(soln3(nums2, k2))


def soln4(nums: List[int], k: int) -> int:
    def partition(nums: List[int], left: int, right: int) -> List[int]:
        pivot = nums[right]
        partition_idx = left - 1
        for idx in range(left, right):
            if nums[idx] <= pivot:
                partition_idx += 1
                nums[partition_idx], nums[idx] = nums[idx], nums[partition_idx]
        nums[partition_idx + 1], nums[right] = nums[right], nums[partition_idx + 1]
        return partition_idx + 1

    def quick_select(nums: List[int], left: int, right: int, idx: int) -> List[int]:
        if len(nums) == 1:
            return nums
        if left < right:
            partition_idx = partition(nums, left, right)
            if partition_idx == idx:
                return nums[partition_idx]
            elif partition_idx > idx:
                return quick_select(nums, left, partition_idx - 1, idx)
            else:
                return quick_select(nums, partition_idx + 1, right, idx)

    idx_to_find = len(nums) - k
    quick_select(nums, 0, len(nums) - 1, idx_to_find)
    return nums[idx_to_find]


print(soln4(nums1, k1))
print(soln4(nums2, k2))
