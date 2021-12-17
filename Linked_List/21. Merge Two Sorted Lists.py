# Leetcode 
# 21. Merge Two Sorted Lists
'''
Merge two sorted linked lists and return it as a [sorted list]. 
The list should be made by splicing together the nodes of the first two lists.
'''
# class ListNode:
from typing import List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# creating List
# l1 - [1,2,4]
l1 = ListNode(1, None)
l1.next = ListNode(2, None)
l1.next.next = ListNode(4, None)

# l2 - [1,3,4]
l2 = ListNode(1, None)
l2.next = ListNode(3, None)
l2.next.next = ListNode(4, None)


# using List
def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
    if l1 is None and l2 is None:  # case [], []
        return None
    elif l1 is None and l2 is not None:  # case l1 = []
        return l2
    elif l1 is not None and l2 is None:  # case l2 = []
        return l1
    else:
        # Merged as list
        merged_list = []
        cur_node1, cur_node2 = l1, l2  # holding current node
        while cur_node1:
            merged_list.append(cur_node1.val)
            cur_node1 = cur_node1.next

        while cur_node2:
            merged_list.append(cur_node2.val)
            cur_node2 = cur_node2.next
        merged_list.sort()

        # Making linked list
        head = linked_list = ListNode(merged_list[0]) # head hold first cursor
        for num in merged_list[1:]:
            linked_list.next = ListNode(num)
            linked_list = linked_list.next
        return head

result = mergeTwoLists(l1, l2)  #output: [1,1,2,3,4,4]
prn = ''
while result:
    prn += str(result.val) + '->'
    result = result.next
print(prn[:-2])

# using recursive
class solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if (not l1) or (l2 and (l1.val > l2.val)):
            l1, l2 = l2, l1
        if l1:
            l1.next = self.mergeTwoLists(l1.next, l2)
        return l1
