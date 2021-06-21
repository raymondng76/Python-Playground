# 206
# Given the head of a single linked list, reverse the list and return the reversed list.
from typing import List, Tuple


class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse(head: Node) -> Tuple[Node, List[int]]:
    reverse_list = []
    prev_node = None
    curr_node = head
    while curr_node:
        reverse_list.append(curr_node.val)
        next_node = curr_node.next
        curr_node.next = prev_node
        prev_node = curr_node
        curr_node = next_node
    return (prev_node, reverse_list[::-1])


input1 = Node(
    val=1,
    next=Node(
        val=2,
        next=Node(
            val=3,
            next=Node(
                val=4,
                next=Node(
                    val=5,
                    next=None
                )
            )
        )
    )
)
input2 = Node(val=3)


n, rl = reverse(input1)
print(n.val)
print(rl)

n, rl = reverse(input2)
print(n.val)
print(rl)
