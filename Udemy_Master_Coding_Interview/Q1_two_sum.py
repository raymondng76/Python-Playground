from typing import List


def brute_force_two_sum(input_nums: List[int], target_val: int) -> List[int]:
    p1 = 0
    p2 = 1
    while p1 < len(input_nums):
        curr_val = input_nums[p1]
        while p2 < len(input_nums):
            curr_sum = curr_val + input_nums[p2]
            if curr_sum == target_val:
                return [p1, p2]
            p2 += 1
        p1 += 1
        p2 = p1 + 1
    return None


input_nums = [1, 3, 7, 9, 2]
target_val = 11
print(brute_force_two_sum(input_nums, target_val))


def two_sum(input_nums: List[int], target_val: int) -> List[int]:
    compliment = {}
    compliment[target_val - input_nums[0]] = 0
    for idx in range(1, len(input_nums)):
        curr_compliment = target_val - input_nums[idx]
        if input_nums[idx] in compliment.keys():
            return [compliment[input_nums[idx]], idx]
        compliment[curr_compliment] = idx
    return None


print(two_sum(input_nums, target_val))


def two_sum_simple(input_nums: List[int], target_val: int) -> List[int]:
    comp = {}
    for idx, val in enumerate(input_nums):
        if val in comp.keys():
            return [comp[val], idx]
        comp[target_val - val] = idx
    return None


print(two_sum_simple(input_nums, target_val))
