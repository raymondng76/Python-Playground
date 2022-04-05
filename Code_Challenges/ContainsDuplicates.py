# return true if any value appears at least twice in the array, else return false
from utils import timer


@timer
def containsDuplicate(nums):
    sorted_lst = sorted(nums)  # sorted first so same values are side by side
    first_pt = 0
    sec_pt = 1  # second pointer is one step in front
    while sec_pt < len(nums):
        if sorted_lst[first_pt] == sorted_lst[sec_pt]:  # if side by side, same values will be true here
            return True
        first_pt += 1  # increase both pointers together
        sec_pt += 1
    return False


nums = [1, 2, 3, 4]
print(containsDuplicate(nums))
