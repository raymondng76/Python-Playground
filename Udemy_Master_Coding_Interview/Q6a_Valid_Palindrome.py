# 125
# Given string, determine if it is a palindrome, only alphanumeric and ignore case
import string


def brute_force_valid_palindrome(s: str) -> bool:
    for punc in string.punctuation:
        s = s.replace(punc, "")
    s = s.lower()
    s = s.replace(" ", "")
    return s == s[::-1]


input1 = "A man, a plan, a canal: Panama"  # True
input2 = "aaabaaa"  # True
input3 = "race a car"  # False
input4 = "aabbaa"  # True
input5 = "a"  # True
input6 = ""  # True
input7 = "abc"  # False

print(brute_force_valid_palindrome(input1))
print(brute_force_valid_palindrome(input2))
print(brute_force_valid_palindrome(input3))
print(brute_force_valid_palindrome(input4))
print(brute_force_valid_palindrome(input5))
print(brute_force_valid_palindrome(input6))
print(brute_force_valid_palindrome(input7))


def soln1(s: str) -> bool:
    if len(s) <= 1:
        return True
    for punc in string.punctuation:
        s = s.replace(punc, "")
    s = s.lower()
    s = s.replace(" ", "")

    pt1 = 0
    pt2 = len(s) - 1
    while pt1 < pt2:
        if s[pt1] != s[pt2]:
            return False
        pt1 += 1
        pt2 -= 1
    return True


print(soln1(input1))
print(soln1(input2))
print(soln1(input3))
print(soln1(input4))
print(soln1(input5))
print(soln1(input6))
print(soln1(input7))


def soln2(s: str) -> bool:
    if len(s) <= 1:
        return True
    for punc in string.punctuation:
        s = s.replace(punc, "")
    s = s.lower()
    s = s.replace(" ", "")

    if len(s) % 2 == 0:
        pt1 = int(len(s) / 2 - 1)
        pt2 = int(pt1 + 1)
    else:
        pt1 = int(len(s) // 2 - 1)
        pt2 = int(len(s) // 2 + 1)

    while pt1 >= 0 and pt2 < len(s):
        if s[pt1] != s[pt2]:
            return False
        pt1 -= 1
        pt2 += 1
    return True


print(soln2(input1))
print(soln2(input2))
print(soln2(input3))
print(soln2(input4))
print(soln2(input5))
print(soln2(input6))
print(soln2(input7))
