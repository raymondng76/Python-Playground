# 92
# Given head of singly linked list and two int, left and right where left <= right.
# Reverse the nodes of the list from postion left to position right and return reverse list
from typing import List


class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def print_linked_list(head: Node) -> List[int]:
    node_list = []
    curr_node = head
    while curr_node:
        node_list.append(curr_node.val)
        curr_node = curr_node.next
    return node_list


def reverse(head: Node, left: int, right: int) -> Node:
    """
    Only for linked list in running order
    """
    curr_pos = head.val
    curr_node = head
    start = head

    while curr_pos < left:
        start = curr_node
        curr_node = curr_node.next
        curr_pos += 1

    new_list = None
    tail = curr_node
    while(curr_pos >= left and curr_pos <= right):
        next_node = curr_node.next
        curr_node.next = new_list
        new_list = curr_node
        curr_node = next_node
        curr_pos += 1

    start.next = new_list
    tail.next = curr_node
    return head if left > 1 else new_list


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
input2 = Node(
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
left1, right1 = 2, 4  # [1, 4, 3, 2, 5, None]
left2, right2 = 1, 5  # [14, 13, 12, 11, 10, None]

print(print_linked_list(reverse(input1, left1, right1)))
print(print_linked_list(reverse(input2, left2, right2)))
