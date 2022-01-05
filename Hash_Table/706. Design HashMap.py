# LeetCode 706. Design HashMap
'''
MyHashMap() initializes the object with an empty map.
void put(int key, int value) inserts a (key, value) pair into the HashMap. If the key already exists in the map, update the corresponding value.
int get(int key) returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key.
void remove(key) removes the key and its corresponding value if the map contains the mapping for the key.
'''

import collections

class ListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class MyHashMap:
    def __init__(self):
        self.size = 1000
        self.table = collections.defaultdict(ListNode)

    def put(self, key: int, value: int) -> None:
        index = key % self.size
        if self.table[index].value == None:
            self.table[index] = ListNode(key,value)
            return
        
        p = self.table[index]
        while p:
            if p.key == key:
                p.value = value
                return
            if p.next == None:
                break
            p = p.next
        p.next = ListNode(key, value)


    def get(self, key: int) -> int:
        index = key % self.size
        if self.table[index].value == None:
            return -1
        
        p = self.table[index]
        while p:
            if p.key == key:
                return p.value
            p= p.next
        return -1
        
    def remove(self, key: int) -> None:
        index = key % self.size
        if self.table[index].value == None:
            return

        p = self.table[index]
        if p.key == key:
            self.table[index] = ListNode() if p.next == None else p.next
            return
        
        prev = p
        while p:
            if p.key == key:
                prev.next == p.next
                return
            prev, p = p, p.next
        