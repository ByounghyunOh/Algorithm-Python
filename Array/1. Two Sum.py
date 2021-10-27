# Leetcode 
# 1. Two Sum
'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
* target = a + b --> target - a = b
'''

def twoSum(nums: list, target: int) -> list:
    for i in range(len(nums)):
        if target - nums[i] in nums and i != nums.index(target - nums[i]): # not include myself
            return i, nums.index(target - nums[i])

print(twoSum(nums = [2,7,11,15], target = 9))  # Output: [0,1] --> 2 + 7 = 9
print(twoSum(nums = [3,2,4], target = 6))  # Output: [1,2] --> 2 + 4 = 6
print(twoSum(nums = [3,3], target = 6))  # Output: [0,1] --> 2 + 4 = 6

# using dict
def twoSum2(nums: list, target: int) -> list:
    dic = {}
    for i in range(len(nums)):
        if target - nums[i] not in dic:
            dic[nums[i]] = i
        else: # target - a = b
            return i, dic[target - nums[i]]

print(twoSum2(nums = [2,7,11,15], target = 9))  # Output: [0,1] --> 2 + 7 = 9
print(twoSum2(nums = [3,2,4], target = 6))  # Output: [1,2] --> 2 + 4 = 6
print(twoSum2(nums = [3,3], target = 6))  # Output: [0,1] --> 2 + 4 = 6