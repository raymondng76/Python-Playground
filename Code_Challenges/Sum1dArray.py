# Given an array num. We define a running sum or array as runningSum[i]=sum(num[0]...num[i])
# Input: nums = [1,2,3,4]
# Output: [1,3,6,10]
# Explanation: [1, 1+2, 1+2+3, 1+2+3+4]

from typing import List
from rich.console import Console

console = Console()


def main(num: List[int]) -> List[int]:
    runningSum = []
    for i in range(len(num)):
        runningSum.append(sum(num[: i + 1]))
    return runningSum

def main2(num: List[int]) -> List[int]:
    return [sum(num[: i + 1]) for i in range(len(num))]

if __name__ == "__main__":
    console.print(main([2, 4, 8, 16]))
    console.print(main2([22, 44, 88, 1616]))
