# return indices of two numbers from array which adds up to target

def twoSum(nums, target):
    comp_set = {}
    for idx, val in enumerate(nums):
        if val in comp_set.keys():
            return [idx, comp_set[val]]
        comp_set[target - val] = idx
    return None


nums1 = [2, 7, 11, 15]
target1 = 9
print(twoSum(nums1, target1))

nums2 = [3, 2, 4]
target2 = 6
print(twoSum(nums2, target2))

nums3 = [3, 3]
target3 = 6
print(twoSum(nums3, target3))

nums4 = [2, 8, 11, 15]
target4 = 9
print(twoSum(nums4, target4))
