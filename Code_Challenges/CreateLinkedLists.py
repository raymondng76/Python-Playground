class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = self.head
            self.length = 1
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.length += 1

    def prepend(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            self.length = 1
        else:
            new_node.next = self.head
            self.head = new_node
            self.length += 1

    def insert(self, index, data):
        if index == 0:
            self.prepend(data)
            return
        if index == self.length:
            self.append(data)
            return

        new_node = Node(data)
        i = 0
        temp_node = self.head
        while i < self.length:
            if i == index - 1:
                temp_node.next, new_node.next = new_node, temp_node.next
                self.length += 1
            temp_node = temp_node.next
            i += 1

    def remove(self, index):
        if index >= self.length:
            raise ValueError(f"Index {index} requested exceed length of linked list!")
        if index == 0:
            self.head = self.head.next
            self.length -= 1
            return

        i = 0
        temp_node = self.head
        while i < self.length:
            if i == index - 1:
                temp_node.next = temp_node.next.next
                self.length -= 1
                return
            temp_node = temp_node.next
            i += 1

    def print(self):
        temp_node = self.head
        while temp_node is not None:
            print(temp_node.data, end=' ')
            temp_node = temp_node.next
        print(f'Length = {self.length}')

    def reverse(self):
        prev_node = None
        self.tail = self.head
        while self.head is not None:
            temp_node = self.head
            self.head = self.head.next
            temp_node.next = prev_node
            prev_node = temp_node
        self.head = temp_node


ll = SinglyLinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)
ll.append(5)
ll.insert(2, 88)
ll.insert(4, 99)
ll.append(111)
ll.prepend(222)
ll.remove(2)
ll.print()
ll.reverse()
ll.print()
