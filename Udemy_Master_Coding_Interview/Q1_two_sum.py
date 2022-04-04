# 1
# Arr of int and a target int. return indices of two numbers such that they add up to target.
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


if __name__ == "__main__":
    import timeit

    su = "from __main__ import brute_force_two_sum"

    s = """
input_nums = [1, 3, 7, 9, 2]
target_val = 11
brute_force_two_sum(input_nums, target_val)
    """

    print("brute_force_two_sum")
    print(timeit.timeit(setup=su, stmt=s, number=100))

    su = "from __main__ import two_sum"

    s = """
input_nums = [1, 3, 7, 9, 2]
target_val = 11
two_sum(input_nums, target_val)
    """

    print("two_sum")
    print(timeit.timeit(setup=su, stmt=s, number=100))

    su = "from __main__ import two_sum_simple"

    s = """
input_nums = [1, 3, 7, 9, 2]
target_val = 11
two_sum_simple(input_nums, target_val)
    """

    print("two_sum_simple")
    print(timeit.timeit(setup=su, stmt=s, number=100))
