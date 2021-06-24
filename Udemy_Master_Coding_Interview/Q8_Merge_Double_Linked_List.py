# 430
# Given doubly linked list in addition to next and previous pointers, it have a child pointer
# which may or may not point to a separate doubly linked list.
# Child lists may have one or more children of their own.
# Flatten list so that all the nodes appear in a single level, doubly linked list.


class Node:
    def __init__(self, val, prev_node=None, next_node=None, child_node=None):
        self.val = val
        self.prev = prev_node
        self.next = next_node
        self.child = child_node


def get_test_node():
    node1 = Node(val=1)
    node2 = Node(val=2, prev_node=node1)
    node1.next = node2
    node3 = Node(val=3, prev_node=node2)
    node2.next = node3
    node4 = Node(val=4, prev_node=node3)
    node3.next = node4
    node5 = Node(val=5, prev_node=node4)
    node4.next = node5
    node6 = Node(val=6, prev_node=node5)
    node5.next = node6

    node7 = Node(val=7, prev_node=node3)
    node3.child = node7
    node8 = Node(val=8, prev_node=node7)
    node7.next = node8
    node9 = Node(val=9, prev_node=node8)
    node8.prev = node9
    node10 = Node(val=10, prev_node=node9)
    node9.next = node10

    node11 = Node(val=11, prev_node=node8)
    node8.child = node11
    node12 = Node(val=12, prev_node=node11)
    node11.next = node12

    return node1


# def make_lists(array):
#     '''
#     https://replit.com/@karencfisher/doublelist#main.py
#     Recursively generates the complete graph from given serialization
#     Parameter:
#     array - serialization of the list as Python list
#     Returns:
#     head to the top most list (first node of the
#     graph)
#     '''
#     head = None
#     prev = None
#     i = 0
#     while i < len(array):
#         if array[i] is not None:
#             node = Node(val=array[i], prev=prev)
#             if prev is None:
#                 head = prev = node
#             else:
#                 prev.next = node
#                 prev = node
#             i += 1
#         else:
#             node = head
#             end = False
#             while array[i] == None:
#                 if node.next is None:
#                     end = True
#                 else:
#                     node = node.next
#                 i += 1
#             if end:
#                 node.child = make_lists(array[i:])
#             else:
#                 node.prev.child = make_lists(array[i:])
#             break
#     return head


# def strLists(head, lists):
#     '''
#     https://replit.com/@karencfisher/doublelist#main.py
#     Helper function to recursively serialize the graph prior to visualization. It's an interim step and
#     only meant to be called by the printLists function.

#     Parameters:
#     head - head of the present list
#     lists - the serialization being built recursively (passed by reference)

#     Returns:
#     None (lists is updated in place).
#     '''
#     if head is None:
#         return
#     nodes = []
#     while head:
#     nodes.append(str(head.val))
#     if head.child is not None:
#         nodes.append('|')
#         strLists(head.child, lists)
#     head = head.next
#     lists.append(nodes)


# def printLists(head):
#     '''
#     https://replit.com/@karencfisher/doublelist#main.py
#     Visualizes the entire graph
#     Parameter:
#     head - the top most Node
#     '''
#     lists = []
#     strLists(head, lists)
#     if lists == []:
#     print(None)
#     return
#     previndent = 0
#     for j, l in enumerate(lists[::-1]):
#     count = -1
#     indent = 0
#     s = []
#     for i in range(len(l)):
#         if l[i] != '|':
#         s.append(l[i])
#         count += 1
#         else:
#         indent = count * 4
#         child = count
#     print('---'.join(s))
#     if  len(lists) > 1 and j < len(lists) - 1:
#         previndent += indent
#         indentation = ''.join([' '] * previndent)
#         if len(l[0]) > 1:
#         indentation += ''.join([' '] * child)
#         print(indentation + '|')
#         print(indentation, end='')

# def checkLinks(head, lists=None):
#     '''
#     https://replit.com/@karencfisher/doublelist#main.py
#     Verifies that all lists can be traversed in both directions.

#     Parameter:
#     head - top most Node

#     Returns:
#     Boolean, True if all lists traversable, False if not.
#     '''
#     if head is None:
#     return True
#     if lists is None:
#     lists = []
#     stack = []
#     result = True
#     node = head
#     while node is not None:
#     if node.child is not None:
#         checkLinks(node.child, lists)
#     stack.append(node)
#     prev = node
#     node = node.next
#     while prev is not None:
#     if len(stack) == 0 or stack.pop() != prev:
#         result = False
#     prev = prev.prev
#     lists.append(result)
#     return all(lists)


# Example to show usage
# array = [1,2,3,4,5,6,null,null,null,7,8,9,10,null,null,11,12]
# head = makeLists(array)
# printLists(head)
# print(checkLinks(head))


def soln(head: Node):
    if not head:
        return head
    curr_node = head
    while curr_node is not None:
        if curr_node.child is None:
            curr_node = curr_node.next
        else:
            tail = curr_node.child
            while tail.next is not None:
                tail = tail.next
            tail.next = curr_node.next
            if tail.next is not None:
                tail.next.prev = tail
            curr_node.next = curr_node.child
            curr_node.next.prev = curr_node
            curr_node.child = None
    return head


input1 = get_test_node()
print(soln(input1).val)
