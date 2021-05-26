# Print all subsets of a given list or set

def all_subsets(given_array):
    subset = [None] * len(given_array)
    helper(given_array, subset, 0)


def print_set(subset):
    result = [i for i in subset if i]
    print(result)


def helper(given_array, subset, idx):
    if idx == len(given_array):
        print_set(subset)
    else:
        subset[idx] = None
        helper(given_array, subset, idx + 1)
        subset[idx] = given_array[idx]
        helper(given_array, subset, idx + 1)


all_subsets([1, 2, 3])
