# return an array after rotated by k times
# Example:
# Input: nums = [1,2,3,4,5,6,7], k = 3
# Output: [5,6,7,1,2,3,4]
# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]

def rotateArray(nums, k):
    for _ in range(k):
        temp = nums.pop()
        nums.insert(0, temp)
    return nums


nums = [1, 2, 3, 4, 5, 6, 7]
k = 3

print(rotateArray(nums, k))


def rotateArray2(nums, k):
    for _ in range(k):
        nums = nums[:-1] + [nums[-1]]
    return nums


print(rotateArray2(nums, k))
