def merge(left, right):
    result = []
    left_idx = 0
    right_idx = 0
    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] < right[right_idx]:
            result.append(left[left_idx])
            left_idx += 1
        else:
            result.append(right[right_idx])
            right_idx += 1
    return result + left[left_idx:] + right[right_idx:]


def mergesort(arr):
    if len(arr) == 1:
        return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    return merge(mergesort(left), mergesort(right))


arr = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
print(mergesort(arr))
