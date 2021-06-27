# 232
# Implement a first in first out (FIFO) queue using only 2 stacks.
# Implemented queue should support push, peek, pop and empty


class MyQueue:
    def __init__(self):
        self.append_stack = []
        self.pop_stack = []
        self.len = 0

    def push(self, x: int) -> None:
        self.append_stack.append(x)
        self.len += 1

    def pop(self) -> int:
        val = None
        if not self.empty():
            if not self.pop_stack:
                self._fill_pop_stack()
            val = self.pop_stack.pop()
            self.len -= 1
        return val

    def peek(self) -> int:
        if self.empty():
            return None
        if not self.pop_stack:
            self._fill_pop_stack()
        return self.pop_stack[-1]

    def empty(self) -> bool:
        return self.len == 0

    def _fill_pop_stack(self):
        while(self.append_stack):
            val = self.append_stack.pop()
            self.pop_stack.append(val)


mq = MyQueue()
mq.push(1)
mq.push(2)
print(mq.peek())
print(mq.pop())
print(mq.empty())
