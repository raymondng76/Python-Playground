# 844
# two strings, return true if they are equal when both typed into empty text editors
# '#' means backspace

def brute_force_typed_out_strings(s: str, t: str) -> bool:
    s_arr = []
    t_arr = []
    for s_str in s:
        if s_str != '#':
            s_arr.append(s_str)
        else:
            if len(s_arr) != 0:
                s_arr.pop()
    for t_str in t:
        if t_str != '#':
            t_arr.append(t_str)
        else:
            if len(t_arr) != 0:
                t_arr.pop()
    s_out = "".join(s_arr)
    t_out = "".join(t_arr)
    return s_out == t_out


s1, t1 = "ab#z", "az#z"  # True
s2, t2 = "abc#d", "acc#c"  # False
s3, t3 = "x#y#z#", "a##"  # True
s4, t4 = "a###b", "b"  # True
s5, t5 = "Ab#z", "ab#z"  # False
s6, t6 = "xywrrmp", "xywrrmu#p"  # True
s7, t7 = "ab##", "c#d#"  # True
s8, t8 = "abc#d", "abzz##d"  # True

print(brute_force_typed_out_strings(s1, t1))
print(brute_force_typed_out_strings(s2, t2))
print(brute_force_typed_out_strings(s3, t3))
print(brute_force_typed_out_strings(s4, t4))
print(brute_force_typed_out_strings(s5, t5))


def brute_force_typed_out_strings2(s: str, t: str) -> bool:
    def process_strings(input_string: str) -> str:
        arr = []
        for in_str in input_string:
            if in_str != '#':
                arr.append(in_str)
            else:
                if len(arr) != 0:
                    arr.pop()
        return "".join(arr)
    final_s = process_strings(s)
    final_t = process_strings(t)
    if len(final_s) != len(final_t):
        return False
    return final_s == final_t


print(brute_force_typed_out_strings2(s1, t1))
print(brute_force_typed_out_strings2(s2, t2))
print(brute_force_typed_out_strings2(s3, t3))
print(brute_force_typed_out_strings2(s4, t4))
print(brute_force_typed_out_strings2(s5, t5))


def typed_out_strings_non_optimal(s: str, t: str) -> bool:
    s_pt = len(s) - 1
    t_pt = len(t) - 1
    s_hold = 0
    t_hold = 0
    s_out = []
    t_out = []
    while s_pt >= 0 or t_pt >= 0:
        if s_pt >= 0:
            if s[s_pt] != '#':
                if s_hold != 0:
                    s_hold -= 1
                    s_pt -= 1
                    continue
                s_out.append(s[s_pt])
                s_pt -= 1
            else:
                s_hold += 1
                s_pt -= 1
        if t_pt >= 0:
            if t[t_pt] != '#':
                if t_hold != 0:
                    t_hold -= 1
                    t_pt -= 1
                    continue
                t_out.append(t[t_pt])
                t_pt -= 1
            else:
                t_hold += 1
                t_pt -= 1
    return "".join(s_out) == "".join(t_out)


print(typed_out_strings_non_optimal(s1, t1))
print(typed_out_strings_non_optimal(s2, t2))
print(typed_out_strings_non_optimal(s3, t3))
print(typed_out_strings_non_optimal(s4, t4))
print(typed_out_strings_non_optimal(s5, t5))
print(typed_out_strings_non_optimal(s6, t6))
print(typed_out_strings_non_optimal(s7, t7))


def typed_out_strings_non_optimal2(s: str, t: str) -> bool:
    s_pt = len(s) - 1
    t_pt = len(t) - 1
    s_hold = 0
    t_hold = 0
    while s_pt >= 0 or t_pt >= 0:
        if s[s_pt] == '#' or t[t_pt] == '#':
            if s[s_pt] == '#' and s_pt >= 0:
                s_hold += 2
                while s_hold > 0 and s_pt >= 0:
                    s_pt -= 1
                    s_hold -= 1
                    if s[s_pt] == '#':
                        s_hold += 2
            if t[t_pt] == '#' and t_pt >= 0:
                t_hold += 2
                while t_hold > 0 and t_pt >= 0:
                    t_pt -= 1
                    t_hold -= 1
                    if t[t_pt] == '#':
                        t_hold += 2
        else:
            if s[s_pt] != t[t_pt]:
                return False
            else:
                s_pt -= 1
                t_pt -= 1
    return True


print(typed_out_strings_non_optimal2(s1, t1))
print(typed_out_strings_non_optimal2(s2, t2))
print(typed_out_strings_non_optimal2(s3, t3))
print(typed_out_strings_non_optimal2(s4, t4))
print(typed_out_strings_non_optimal2(s5, t5))
print(typed_out_strings_non_optimal2(s6, t6))
print(typed_out_strings_non_optimal2(s7, t7))
print(typed_out_strings_non_optimal2(s8, t8))


def typed_out_strings_stack(s: str, t: str) -> bool:
    def build_strings(input_str):
        stack = []
        for char in input_str:
            if not stack and char == '#':
                continue
            elif char == '#':
                stack.pop()
            else:
                stack.append(char)
        return "".join(stack)
    return build_strings(s) == build_strings(t)


print(typed_out_strings_stack(s1, t1))
print(typed_out_strings_stack(s2, t2))
print(typed_out_strings_stack(s3, t3))
print(typed_out_strings_stack(s4, t4))
print(typed_out_strings_stack(s5, t5))
print(typed_out_strings_stack(s6, t6))
print(typed_out_strings_stack(s7, t7))
print(typed_out_strings_stack(s8, t8))


def typed_out_strings(s: str, t: str) -> bool:
    import itertools
    def F(input_str: str):
        skip = 0
        for x in reversed(input_str):
            if x == '#':
                skip += 1
            elif skip:
                skip -= 1
            else:
                yield x
    return all(x == y for x, y in itertools.zip_longest(F(s), F(t)))


print(typed_out_strings(s1, t1))
print(typed_out_strings(s2, t2))
print(typed_out_strings(s3, t3))
print(typed_out_strings(s4, t4))
print(typed_out_strings(s5, t5))
print(typed_out_strings(s6, t6))
print(typed_out_strings(s7, t7))
print(typed_out_strings(s8, t8))
