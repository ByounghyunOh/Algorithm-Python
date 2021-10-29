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
