# 142
# Given a linked list, return the node where the cycle begins, if no cycle, return None

from typing import Union


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def brute_force_soln(head: Node) -> Union[Node, None]:
    if head is None:
        return head
    curr_node = head
    seen_nodes = set()
    while curr_node not in seen_nodes:
        if curr_node.next is None:
            return None
        seen_nodes.add(curr_node)
        curr_node = curr_node.next
    return curr_node


node1 = Node(val=3)
node2 = Node(val=2)
node1.next = node2
node3 = Node(val=0)
node2.next = node3
node4 = Node(val=-4)
node3.next = node4
node4.next = node2

print(brute_force_soln(node1).val)


def soln(head: Node) -> Union[Node, None]:
    if head is None or head.next is None:
        return None
    fast = head
    slow = head
    while(True):
        if fast.next is None:
            return None
        fast = fast.next
        if fast.next is None:
            return None
        fast = fast.next
        slow = slow.next
        if fast == slow:
            break
    new_head = head
    while(True):
        if new_head == slow:
            return new_head
        new_head = new_head.next
        slow = slow.next


print(soln(node1).val)
