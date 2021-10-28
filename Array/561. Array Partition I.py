# Leetcode 
# 561. Array Partition I
'''
Given an integer array nums of 2n integers, group these integers into n pairs (a1, b1), (a2, b2), ..., (an, bn) 
such that the sum of min(ai, bi) for all i is maximized. Return the maximized sum.
'''
# even numbers total
def arrayPairSum(nums: list) -> int:
    nums.sort()
    return sum(nums[::2])

print(arrayPairSum([1,4,3,2]))
print(arrayPairSum([6,2,6,5,1,2]))