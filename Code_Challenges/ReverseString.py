# reverse string

import time


def reverseStr(str):
    return str[::-1]


def reverseStr2(str):
    result = ''
    for s in range(len(str) - 1, -1, -1):
        result += str[s]

    return result


testString = 'Hi My Name Is Someone'
rs1_start = time.time()
print(reverseStr(testString))
rs1_end = time.time()
rs2_start = time.time()
print(reverseStr2(testString))
rs2_end = time.time()

print(f"RS1 Time {rs1_end - rs1_start}")
print(f"RS2 Time {rs2_end - rs2_start}")

emptyString = ""
print(reverseStr(emptyString))
print(reverseStr2(emptyString))
