# Merge sorted arrays

def mergeSortedArrays(arr1, arr2):
    if len(arr1) == 0 or len(arr2) == 0:
        return arr1 + arr2

    arr1_pt = 0
    arr2_pt = 0
    result = []
    while ((arr1_pt <= len(arr1) - 1) and (arr2_pt <= len(arr2) - 1)):
        if arr1[arr1_pt] > arr2[arr2_pt]:
            result.append(arr2[arr2_pt])
            arr2_pt += 1
        else:
            result.append(arr1[arr1_pt])
            arr1_pt += 1
    return result + arr2[arr2_pt:] + arr1[arr1_pt:]


arr1 = [0, 3, 4, 41]
arr2 = [4, 5, 30]

print(mergeSortedArrays(arr1, arr2))

arr3 = []
arr4 = [22, 23, 24]

print(mergeSortedArrays(arr3, arr4))
