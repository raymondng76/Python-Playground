# 3
# Given string, find length of the longest substring without repeating characters

def brute_force_soln(input_str: str) -> int:
    max_length = 0
    for i in range(len(input_str)):
        seen = []
        seen.append(input_str[i])
        max_length = max(max_length, len(seen))
        for j in range(i+1, len(input_str)):
            if input_str[j] not in seen:
                seen.append(input_str[j])
                max_length = max(max_length, len(seen))
            else:
                break
    return max_length


input1 = 'abcabcbb'  # 3
input2 = 'bbbbb'  # 1
input3 = 'pwwkew'  # 3
input4 = 'aab'  # 2
input5 = 'dvdf'  # 3
input6 = 'abcbdaac'  # 4

print(brute_force_soln(input1))
print(brute_force_soln(input2))
print(brute_force_soln(input3))


def soln(input_str: str) -> int:
    if len(input_str) <= 1:
        return len(input_str)
    max_length = 0
    L = 0
    R = 0
    seen = {}
    while R < len(input_str):
        curr_char = input_str[R]
        previous_char = seen.get(curr_char, -1)
        if previous_char >= L:
            L = previous_char + 1
        seen[curr_char] = R
        max_length = max(max_length, R - L + 1)
        R += 1
    return max_length


print(soln(input1))
print(soln(input2))
print(soln(input3))
print(soln(input4))
print(soln(input5))
print(soln(input6))
