# 20
# Given a string containing just the chars '(', ')', '{', '}', '[', ']', determine if input string is valid.

def soln(s: str) -> bool:
    if not s:
        return True
    compliment = {'{': '}', '[': ']', '(': ')'}
    lq = []
    for char in s:
        if char in compliment.keys():
            lq.append(char)
        else:
            try:
                last_char = lq.pop()
            except IndexError:
                return False
            if compliment[last_char] == char:
                continue
            else:
                return False
    return True if len(lq) == 0 else False


input1 = ""  # True
input2 = "{([])}"  # True
input3 = "{([]"  # False
input4 = "{[(])}"  # False
input5 = "{[]()}"  # True

print(soln(input1))
print(soln(input2))
print(soln(input3))
print(soln(input4))
print(soln(input5))
