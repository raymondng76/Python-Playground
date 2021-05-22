# given an array, move all zeros to the back of the array without copy

def moveZeroes(nums):
    idx = 0
    nums_len = len(nums)
    for _ in range(nums_len):
        if nums[idx] == 0:
            nums.pop(idx)
            nums.append(0)
        else:
            idx += 1


nums = [0, 1, 0, 3, 12]
moveZeroes(nums)