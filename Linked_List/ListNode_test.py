# class ListNode:
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# creating List - [1,2,2,1])
ln = ListNode(1, None)
ln.next = ListNode(2, None)
ln.next.next = ListNode(2, None)
ln.next.next.next = ListNode(1, None)

# Normal loop
def loopList(node: ListNode) -> list:
    ln_list = []
    current_node = node  # set current node

    while current_node is not None:
        ln_list.append(current_node.val)
        current_node = current_node.next
    print(ln_list)        

loopList(ln)

# Reccursive
class recursive:
    ln_list = []
    def recursive_list(self, node: ListNode) -> list:
        current_node = node
        if current_node:
            self.ln_list.append(current_node.val)
            self.recursive_list(current_node.next)
        return self.ln_list
rc = recursive()
print(rc.recursive_list(ln))

print('--- # Making Linked List from list ---')
# class ListNode:
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Making linked List(=ListNode) from list
def make_linked_list(nums: list) -> ListNode:
    # head hold start cursor of list
    head = linked_list = ListNode(nums[0])
    for num in nums[1:]:
        linked_list.next = ListNode(num)  # linking next ListNode with val 
        linked_list = linked_list.next  # Move cursor
    return head # return head cursor

result = make_linked_list([1,2,3,4])

# checking the linked_list created correctly
prn = ''
while result:
    prn += str(result.val) + '->'
    result = result.next
print(prn[:-2])
