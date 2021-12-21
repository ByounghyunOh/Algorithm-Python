# Leetcode 
# 232. Implement Queue using Stacks
#   Implement a first in first out (FIFO) queue using only two stacks. The implemented queue should support all the functions of a normal queue (push, peek, pop, and empty).

class MyQueue:

    def __init__(self):
        self.stack = []

    # void push(int x) Pushes element x to the back of the queue.
    def push(self, x: int) -> None:
        self.stack.append(x)

    # int pop() Removes the element from the front of the queue and returns it.
    def pop(self) -> int:
        return self.stack.pop(0)

    # int peek() Returns the element at the front of the queue.
    def peek(self) -> int:
        return self.stack[0]

    # boolean empty() Returns true if the queue is empty, false otherwise.
    def empty(self) -> bool:
        if not self.stack:
            return True
        else:
            return False


# Your MyQueue object will be instantiated and called as such:
obj = MyQueue()
obj.push(1)
obj.push(2)
param_1 = obj.peek()
param_2 = obj.pop()
param_3 = obj.empty()
print(param_1, param_2, param_3)
