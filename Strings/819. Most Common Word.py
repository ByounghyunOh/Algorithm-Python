# Leetcode 
# 819. Most Common Word
'''
Given a string paragraph and a string array of the banned words banned, 
return the most frequent word that is not banned. 
It is guaranteed there is at least one word that is not banned, and that the answer is unique.

The words in paragraph are case-insensitive and the answer should be returned in lowercase.
'''

import collections
import re
def mostCommonWord(paragraph: str, banned: list) -> str:
    paragraph = re.sub('[^\w]', ' ', paragraph.lower())  #remove special char and change to lower
    para_list = [para for para in paragraph.split() if para not in banned]  #split and exclude banned word list

    # Count 
    count_dict = {}
    for p in para_list:
        #print(p)
        if p in count_dict.keys():
            count_dict[p] += 1
        else:
            count_dict[p] = 1
    # Sort by value desc
    count_dict = sorted(count_dict.items(), key = lambda item: (item[1]))
    return count_dict[-1][0]
print(mostCommonWord(paragraph = "Bob hit a ball, the hit BALL flew far after it was hit.", banned = ["hit"]))
print(mostCommonWord("Bob. hIt, baLl", ["bob", "hit"]))
print(mostCommonWord("a, a, a, a, b,b,b,c, c",["a"]))


# Using collection Counter class(dict sub class) and most_common() method use. 
import re
from typing import Collection
def mostCommonWord2(paragraph: str, banned: list) -> str:
    para_list = [para for para in re.sub('[^\w]', ' ', paragraph).lower().split() if para not in banned] 

    # Count 
    count = collections.Counter(para_list)

    # Most common
    return count.most_common(1)[0][0]
    
print(mostCommonWord2(paragraph = "Bob hit a ball, the hit BALL flew far after it was hit.", banned = ["hit"]))
print(mostCommonWord2("Bob. hIt, baLl", ["bob", "hit"]))
print(mostCommonWord2("a, a, a, a, b,b,b,c, c",["a"]))