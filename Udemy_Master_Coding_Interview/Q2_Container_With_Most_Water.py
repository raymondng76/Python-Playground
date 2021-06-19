# Arr of pos int where each int represents the height of a vertical line on a chart.
# Find 2 lines which together with the x-axis forms a container that would hold the greatest amount of water.
# Return area of water held.
from typing import List


def brute_force_water_area(levels: List[int]) -> int:
    if len(levels) <= 1:
        return 0
    p1 = 0
    p2 = 1
    max_area = 0
    while p1 < len(levels):
        while p2 < len(levels):
            curr_area = min(levels[p1], levels[p2]) * (p2 - p1)
            if curr_area > max_area:
                max_area = curr_area
            p2 += 1
        p1 += 1
        p2 = p1 + 1
    return max_area


levels = [6, 9, 3, 4, 5, 8]
levels2 = [7, 1, 2, 3, 9]
print(brute_force_water_area(levels))
print(brute_force_water_area(levels2))


def water_area(levels: List[int]) -> int:
    if len(levels) <= 1:
        return 0
    p1 = 0
    p2 = len(levels) - 1
    max_area = 0
    while p1 != p2:
        curr_area = min(levels[p1], levels[p2]) * (p2 - p1)
        if curr_area > max_area:
            max_area = curr_area
        if levels[p2] > levels[p1]:
            p1 += 1
        else:
            p2 -= 1
    return max_area


print(water_area(levels))
print(water_area(levels2))


def water_area2(height: List[int]) -> int:
    front = 0
    back = len(height) - 1
    best_area = (back - front) * height[min(front, back)]
    while(True):
        if back == front:
            return best_area
        if height[front] > height[back]:
            back -= 1
        else:
            front += 1
        curr_area = (back - front) * height[min(back, front)]
        if curr_area > best_area:
            best_area = curr_area


print(water_area2(levels))
print(water_area2(levels2))
