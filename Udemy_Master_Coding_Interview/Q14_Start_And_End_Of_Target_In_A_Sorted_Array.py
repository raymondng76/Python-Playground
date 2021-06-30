# 34
# Given arry of int nums sorted in ascending order, find starting and ending position of given target value.

from typing import List, Tuple


def brute_force_soln(nums: List[int], target: int) -> List[int]:
    left = 0
    right = len(nums) - 1
    low = -1
    high = -1
    while left <= right:
        mid = (left + right) // 2
        val = nums[mid]
        if val == target:
            ileft = mid - 1
            iright = mid + 1
            low = mid
            high = mid
            while ileft >= 0:
                if nums[ileft] == target:
                    low = ileft
                    ileft -= 1
                else:
                    break
            while iright < len(nums):
                if nums[iright] == target:
                    high = iright
                    iright += 1
                else:
                    break
            return [low, high]
        if val < target:
            left = mid + 1
        else:
            right = mid - 1
    return [low, high]


input1 = [5, 7, 7, 8, 8, 10]
target1 = 8  # [3, 4]
input2 = [5, 7, 7, 8, 8, 10]
target2 = 6  # [-1, -1]
input3 = []
target3 = 0  # [-1, -1]
input4 = [1, 3, 3, 5, 5, 5, 8, 9]
target4 = 5  # [3, 5]
input5 = [1, 2, 3, 4, 5, 6]
target5 = 4  # [3, 3]
input6 = [1]
target6 = 1  # [0, 0]


print(brute_force_soln(input1, target1))
print(brute_force_soln(input2, target2))
print(brute_force_soln(input3, target3))
print(brute_force_soln(input4, target4))
print(brute_force_soln(input5, target5))


def soln(nums: List[int], target: int) -> List[int]:
    def binary_search(nums: List[int], target: int) -> Tuple[bool, int]:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            val = nums[mid]
            if val == target:
                return True, mid
            elif val < target:
                left = mid + 1
            else:
                right = mid - 1
        return False, -1

    low = -1
    high = -1
    found, first_found = binary_search(nums, target)
    if found:
        low = first_found
        high = first_found
        while low >= 0:
            left_found, left = binary_search(nums[:low], target)
            if not left_found:
                break
            low = left
        while high < len(nums):
            right_found, right = binary_search(nums[high + 1:], target)
            if not right_found:
                break
            high = (right + high + 1)

    return [low, high]


print(soln(input1, target1))
print(soln(input2, target2))
print(soln(input3, target3))
print(soln(input4, target4))
print(soln(input5, target5))
print(soln(input6, target6))


def soln2(nums: List[int], target: int) -> List[int]:
    def binary_search(nums: List[int], left: int, right: int, target: int) -> int:
        while left <= right:
            mid = (left + right) // 2
            val = nums[mid]
            if val == target:
                return mid
            elif val < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1

    if len(nums) == 0:
        return [-1, -1]
    first_pos = binary_search(nums, 0, len(nums) - 1, target)
    if first_pos == -1:
        return [-1, -1]
    start_pos = first_pos
    end_pos = first_pos
    while start_pos != -1:
        temp1 = start_pos
        start_pos = binary_search(nums, 0, start_pos - 1, target)
    start_pos = temp1
    while end_pos != -1:
        temp2 = end_pos
        end_pos = binary_search(nums, end_pos + 1, len(nums) - 1, target)
    end_pos = temp2
    return [start_pos, end_pos]


print(soln2(input1, target1))
print(soln2(input2, target2))
print(soln2(input3, target3))
print(soln2(input4, target4))
print(soln2(input5, target5))
print(soln2(input6, target6))
