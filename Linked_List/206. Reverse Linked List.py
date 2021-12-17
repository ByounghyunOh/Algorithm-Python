# Leetcode
# 206. Reverse Linked List
'''
Given the head of a singly linked list, reverse the list, and return the reversed list.

'''
# Class linklist node
class ListNode:
    def __init__(self, val = 0, next= None):
        self.val = val
        self.next = next

# Create List
ln = ListNode(1, None)
ln.next = ListNode(2, None)
ln.next.next = ListNode(3, None)
ln.next.next.next = ListNode(4, None)

#Reverse
def reverseList(head: list) -> ListNode:
    node, prev = head, None

    while node:
        next, node.next = node.next, prev
        prev, node = node, next
    return prev

result = reverseList(ln)

# checking the linked_list correctly
prn = ''
while result:
    prn += str(result.val) + '->'
    result = result.next
print(prn[:-2])