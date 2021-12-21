# Leetcode 
# 20. Valid Parentheses 
#   - Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.


def isValid(s: str) -> bool:
    dic = {')':'(', '}':'{', ']': '['}
    q = []

    for c in s:
        if c not in dic:
            q.append(c)
            print(q)
        elif not q or dic[c] != q.pop():
            return False
    return len(q) == 0

        
print(isValid('()[]{}'))
print(isValid('([)]'))
