class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = None


def hasCycle(head):
    if not head:
        return False
    first = head
    second = head
    while(True):
        if not first.next:
            return False
        first = first.next
        if not first.next:
            return False
        first = first.next
        second = second.next
        if first == second:
            return True


def hasCycle2(head):
    if not head or not head.next:
        return False
    record = set()
    record.add(hex(id(head)))
    nextNode = head.next
    while(nextNode):
        nextNode_Address = hex(id(nextNode))
        if nextNode_Address in record:
            return True
        if not head.next:
            return False
        record.add(nextNode_Address)
        nextNode = nextNode.next


ll1 = Node(val=3)
ll2 = Node(val=2)
ll3 = Node(val=0)
ll4 = Node(val=-4)

ll1.next = ll2
ll2.next = ll3
ll3.next = ll4
ll4.next = ll2

print(hasCycle(ll1))
print(hasCycle2(ll1))
