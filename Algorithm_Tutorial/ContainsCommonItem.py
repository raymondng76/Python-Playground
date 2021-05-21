# Return true if both list have common items

def containsCommon(arr1, arr2):
    for a in arr1:
        for b in arr2:
            if a == b:
                return True
    return False


def containsCommon2(arr1, arr2):
    set_arr1 = set(arr1)
    set_arr2 = set(arr2)
    result = set_arr1.intersection(set_arr2)
    if result:
        return True
    else:
        return False


arr1 = ['a', 'b', 'c', 'x']
arr2 = ['z', 'y', 'i']
arr2 = ['z', 'y', 'x']

print(containsCommon(arr1, arr2))
print(containsCommon2(arr1, arr2))
