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
            if lq:
                last_char = lq.pop()
            else:
                return False
            if compliment[last_char] != char:
                return False
    return len(lq) == 0


input1 = ""  # True
input2 = "{([])}"  # True
input3 = "{([]"  # False
input4 = "{[(])}"  # False
input5 = "{[]()}"  # True
input6 = "}[]{"  # False

print(soln(input1))
print(soln(input2))
print(soln(input3))
print(soln(input4))
print(soln(input5))
print(soln(input6))
