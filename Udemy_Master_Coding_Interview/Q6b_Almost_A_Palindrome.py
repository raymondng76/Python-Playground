# 680
# Given a string, return true if string can be palindrome after deleting at most one char
# Consider alphanumeric and case sensitivity
import string


def soln1(s: str) -> bool:
    for punc in string.punctuation:
        s = s.replace(punc, "")
    s = s.replace(" ", "").lower()

    def check_palindrome(ss: str) -> bool:
        pt1 = 0
        pt2 = len(ss) - 1
        while pt1 < pt2:
            if ss[pt1] != ss[pt2]:
                return False
            pt1 += 1
            pt2 -= 1
        return True

    pt1 = 0
    pt2 = len(s) - 1
    while pt1 < pt2:
        if s[pt1] != s[pt2]:
            flag1 = check_palindrome(s[pt1:pt2])
            flag2 = check_palindrome(s[pt1+1:pt2+1])
            return flag1 or flag2
        pt1 += 1
        pt2 -= 1
    return True


input1 = 'aba'          # True
input2 = 'abca'         # True
input3 = 'abc'          # False
input4 = 'race a car'   # True
input5 = 'abccdba'      # True
input6 = 'abcdefdba'    # False
input7 = 'a'            # True
input8 = ''             # True
input9 = 'ab'           # True


print(soln1(input1))
print(soln1(input2))
print(soln1(input3))
print(soln1(input4))
print(soln1(input5))
print(soln1(input6))
print(soln1(input7))
print(soln1(input8))
print(soln1(input9))


def soln2(s: str) -> bool:
    for punc in string.punctuation:
        s = s.replace(punc, "")
    s = s.replace(" ", "").lower()

    def check_palindrome(ss: str, pt1: int, pt2: int) -> bool:
        while pt1 < pt2:
            if ss[pt1] != ss[pt2]:
                return False
            pt1 += 1
            pt2 -= 1
        return True

    pt1 = 0
    pt2 = len(s) - 1
    while pt1 < pt2:
        if s[pt1] != s[pt2]:
            flag1 = check_palindrome(s, pt1, pt2 - 1)
            flag2 = check_palindrome(s, pt1 + 1, pt2)
            return flag1 or flag2
        pt1 += 1
        pt2 -= 1
    return True


print(soln2(input1))
print(soln2(input2))
print(soln2(input3))
print(soln2(input4))
print(soln2(input5))
print(soln2(input6))
print(soln2(input7))
print(soln2(input8))
print(soln2(input9))
