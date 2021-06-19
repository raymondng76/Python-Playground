# 42
# Given an array of int representing an elevation map where width of each bar is 1
# return how much rainwater can be trapped
from typing import List


def brute_force_trap_rainwater(levels: List[int]) -> int:
    rain_count = 0
    for lev in range(1, len(levels) - 1):
        left_max_val = max(levels[:(lev + 1)])
        right_max_val = max(levels[(lev + 1):])
        rain_count += max(0, min(left_max_val, right_max_val) - levels[lev])
    return rain_count


levels1 = [0, 1, 0, 2, 1, 0, 3, 1, 0, 1, 2]  # 8
levels2 = []  # 0
levels3 = [3]  # 0
levels4 = [3, 4, 3]  # 0
levels5 = [5, 0, 3, 0, 0, 0, 2, 3, 4, 2, 1]  # 20


print(brute_force_trap_rainwater(levels1))
print(brute_force_trap_rainwater(levels2))
print(brute_force_trap_rainwater(levels3))
print(brute_force_trap_rainwater(levels4))
print(brute_force_trap_rainwater(levels5))


def trap_rainwater(levels: List[int]) -> int:
    rain_count = 0
    if len(levels) <= 1:
        return rain_count
    p1 = 0
    p2 = len(levels) - 1
    maxLeft = 0
    maxRight = 0
    while p1 != p2:
        if levels[p1] < levels[p2]:
            maxLeft = max(maxLeft, levels[p1])
            rain_count += (maxLeft - levels[p1])
            p1 += 1
        else:
            maxRight = max(maxRight, levels[p2])
            rain_count += (maxRight - levels[p2])
            p2 -= 1
    return rain_count


print(trap_rainwater(levels1))
print(trap_rainwater(levels2))
print(trap_rainwater(levels3))
print(trap_rainwater(levels4))
print(trap_rainwater(levels5))
