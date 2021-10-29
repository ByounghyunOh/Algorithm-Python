# Leetcode 
# 234. Palindrome Linked List
'''
Given the head of a singly linked list, return true if it is a palindrome.
'''
# class ListNode:
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# using deque
import collections
def isPalindrome(head: list) -> bool:
    q = collections.deque()
    current_node = head

    while current_node is not None:
        q.append(current_node.val)
        current_node = current_node.next

    while len(q) > 1:
        if q.popleft() != q.pop():  #if not match not palindrom
            return False
    return True 


# creating List - [1,2,2,1])
ln = ListNode(1, None)
ln.next = ListNode(2, None)
ln.next.next = ListNode(2, None)
ln.next.next.next = ListNode(1, None)

print(isPalindrome(ln))  #output: True

# creating List - [1,2])
#print(isPalindrome([1,2])) #output: False