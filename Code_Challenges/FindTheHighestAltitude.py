# There is a biker going on a road trip. The road trip consists of n + 1 points at different altitudes. The biker starts his trip on point 0 with altitude equal 0.

# You are given an integer array gain of length n where gain[i] is the net gain in altitude between points i​​​​​​ and i + 1 for all (0 <= i < n). Return the highest altitude of a point.

# Example 1
# Input: gain = [-5,1,5,0,-7]
# Output: 1
# Explanation: The altitudes are [0,-5,-4,1,1,-6]. The highest is 1.

# Example 2
# Input: gain = [-4,-3,-2,-1,4,3,2]
# Output: 0
# Explanation: The altitudes are [0,-4,-7,-9,-10,-6,-3,-1]. The highest is 0.

from rich.console import Console
from typing import List

console = Console()


def main(gain: List[int]) -> int:
    trip = [0]
    highest = 0
    for g in gain:
        next = trip[-1] + g
        trip.append(next)
        if next > highest:
            highest = next
    return highest


def main2(gain: List[int]) -> int:
    alt_meter = [0]
    for g in gain:
        alt_meter.append(alt_meter[-1] + g)
    return max(alt_meter)


if __name__ == "__main__":
    console.print(main2([-5, 1, 5, 0, -7]))