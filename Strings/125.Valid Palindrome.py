# Leetcode 
# 125. Given a string s, determine if it is a palindrome, [considering only alphanumeric characters and ignoring cases.]

# Using List
def isPalindrome(s: str) -> bool:
    s_str = []
    for i in s:
        if i.isalnum(): # Validation only num and letter
            s_str.append(i.lower()) # upper case change to lower case
    print(s_str)
    # case that match all chars, and middle one char not match
    while len(s_str) > 1:
        if s_str.pop(0) != s_str.pop():
            return False
    return True
#print(isPalindrome('A man, a plan, a canal: Panama'))
#print(isPalindrome('race a car'))


# Using List with dequeue() -> for better queue, stack O(1)
import collections

def isPalindrome2(s: str) -> bool:
    s_str = collections.deque()

    for i in s:
        if i.isalnum(): # Validation only num and letter
            s_str.append(i.lower()) # upper case change to lower case
    print(s_str)
    # case that match all chars, and middle one char not match
    while len(s_str) > 1:
        if s_str.popleft() != s_str.pop():
            return False
    return True
#print(isPalindrome2('A man, a plan, a canal: Panama'))
#print(isPalindrome2('race a car'))

# Using slice (Fastest)
import re  #Regex
def isPalindrome3(s: str) -> bool:
    s = s.lower()
    # ^ means Not, a-zA-z0-9 is range of regex, '' is what is will be replace.
    # If s is not in [a-zA-Z0-9], replace with '' (same as removed)
    s = re.sub('[^a-z0-9]','',s)
    print(s)
    if s == s[::-1]:
        return True
    else:
        return False
print(isPalindrome3('A man, a plan, a canal: Panama'))
print(isPalindrome3('race a car'))