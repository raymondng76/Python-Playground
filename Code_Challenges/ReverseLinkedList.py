from collections import deque
# from rich.console import Console

# console = Console()
# rprint = console.print


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# def reverseList(head):
#     stack = deque()
#     rprint(f"Push : {head.val}")
#     stack.append(head)
#     while head.next:
#         rprint(f"Push : {head.next.val}")
#         stack.append(head.next)
#     reversedHead = stack.pop()
#     rprint(f"Pop : {reversedHead.val}")
#     temp_node = stack.pop()
#     rprint(f"Pop : {temp_node.val}")
#     reversedHead.next = temp_node
#     while stack:
#         temp_node = stack.pop()
#         temp_node.next = ""


def reverseList2(head):
    prev = None
    curr = head
    while curr:
        nextTemp = curr.next
        curr.next = prev
        prev = curr
        curr = nextTemp
    return prev


if __name__ == "__main__":
    print(reverseList2(ListNode(val=0, next=ListNode(val=2, next=ListNode(val=3)))).val)
