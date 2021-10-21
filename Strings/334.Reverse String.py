# Leetcode 
# 344. Reverse String -         Do not return anything, modify s in-place instead.

# using List reverse() method
def reverseString(s: list) -> None:
    s.reverse()
    print(s)

#reverseString(["h","e","l","l","o"])
#reverseString(["h","a","n","n","a","h"])


# using two point
def reverseString2(s: list) -> None:
    left, right = 0, len(s) - 1
    while (left < right):
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1 # because start from last of list(left)
    print(s)

reverseString2(["h","e","l","l","o"])
reverseString2(["h","a","n","n","a","h"])