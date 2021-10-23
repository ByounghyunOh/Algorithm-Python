# Leetcode 
# 937.Reorder Data in Log Files
'''
The letter-logs come before all digit-logs.
The letter-logs are sorted lexicographically by their contents. 
If their contents are the same, then sort them lexicographically by their identifiers.
The digit-logs maintain their relative ordering.
'''

def reorderLogFiles(logs: list) -> list:
    letters, digits = [], []
    for log in logs:
        if log.split()[1].isdigit():
            #print('digit:',log)
            digits.append(log)
        else:
            letters.append(log)
            #print('letter:', log)
    #print('letter:', letters)
    #print('digit:', digits)
    # only letter need to order, first[1]~ last[-1] will be sort keys, then 0 as key just in case same 
    letters.sort(key=lambda x: (x.split()[1:], x.split()[0])) 
    return letters + digits

print(reorderLogFiles(["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]))
#reorderLogFiles(["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"])