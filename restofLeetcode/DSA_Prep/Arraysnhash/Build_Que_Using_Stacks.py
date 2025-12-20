"""
Here we are building a que using a stack
"""


class MyQueue:

    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:
        self.stack.insert(0, x)
        return self.stack

    def pop(self) -> int:
        tmp = self.stack.pop()
        return tmp

    def peek(self) -> int:
        top = self.stack[-1]
        return top

    def empty(self) -> bool:
        if len(self.stack) == 0:
            return True
        return False

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()