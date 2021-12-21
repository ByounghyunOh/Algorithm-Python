# Leetcode 
# 225. Implement Stack using Queues
#   - Implement a last-in-first-out (LIFO) stack using only two queues. The implemented stack should support all the functions of a normal stack (push, top, pop, and empty).

class MyStack:

    def __init__(self):       
        self.q = []

    def push(self, x: int) -> None:
       self.q.append(x)
    # Delete last element
    def pop(self) -> int:
        return self.q.pop(-1)
    # Return top last element
    def top(self) -> int:
        return self.q[-1]
    # return stack is empty or not
    def empty(self) -> bool:
        if not self.q:  # emtpy
            return True
        else:
            return False


# Your MyStack object will be instantiated and called as such:
obj = MyStack()
obj.push(1)
obj.push(2)
print(obj.q)
param_2 = obj.top()
param_3 = obj.pop()
param_4 = obj.empty()
print(param_2, param_3, param_4)
