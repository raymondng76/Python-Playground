# returns max sum of subarray

def maxSubArray(nums):
    if len(nums) == 1:
        return nums[0]

    mSub = nums[0]
    cSum = 0
    for n in nums:
        if cSum < 0:
            cSum = 0
        cSum += n
        mSub = max(mSub, cSum)
    return mSub


nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(maxSubArray(nums))
