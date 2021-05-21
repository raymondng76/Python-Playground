# Return true if there is a pair of number in the list which sum to the sum_val

def havePairWithSum(arr, sum_val):
    comp = set()
    for val in arr:
        if val in comp:
            return True
        comp.add(sum_val - val)
    return False


arr = [1, 2, 3, 4, 4]
sum = 8


print(havePairWithSum(arr, sum))
