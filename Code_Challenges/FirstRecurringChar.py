
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
print(firstRecurringChar(lst4))
