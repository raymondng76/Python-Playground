# 1249
# Given a string '(', ')' and lower case English characters
# Remove minimal number of '(' or ')' to make a valid string.
# Empty string is also a valid string


def soln(s: str) -> str:
    chars = [c for c in s]
    stack = []
    to_rm = []
    for c in range(len(chars)):
        if chars[c] == '(':
            stack.append(c)
        elif chars[c] == ')':
            if len(stack) == 0:
                to_rm.append(c)
            else:
                stack.pop()
    stack += to_rm
    stack = reversed(sorted(stack))
    if stack:
        for c in stack:
            chars.pop(c)
    return "".join(chars)


input1 = '))(('  # ""
input2 = "a)bc(d)"  # abc(d)
input3 = "(ab(c)d"  # ab(c)d or (abc)d

print(soln(input1))
print(soln(input2))
print(soln(input3))
