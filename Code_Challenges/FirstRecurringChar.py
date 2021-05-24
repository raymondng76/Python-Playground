import time


def firstRecurringChar(lst):
    char_set = set()
    for i in lst:
        if i in char_set:
            return i
        else:
            char_set.add(i)
    return None


lst1 = 'ABCA'
lst2 = 'BCABA'
lst3 = 'ABC'
lst4 = 'DBCABA'


print(firstRecurringChar(lst1))
print(firstRecurringChar(lst2))
print(firstRecurringChar(lst3))
start = time.time()
print(firstRecurringChar(lst4))
end = time.time()
print(f"time : {end - start}")


def firstRecurringChar2(lst):
    char_dict = {}
    for i in lst:
        if i in char_dict.keys():
            return i
        else:
            char_dict[i] = True
    return None


# print(firstRecurringChar2(lst1))
# print(firstRecurringChar2(lst2))
# print(firstRecurringChar2(lst3))

start = time.time()
print(firstRecurringChar2(lst4))
end = time.time()
print(f"time : {end - start}")
