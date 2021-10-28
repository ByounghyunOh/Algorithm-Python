# Leetcode 
# 121. Best Time to Buy and Sell Stock
'''
You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
'''

# brutal force
def maxProfit(prices: list) -> int:
    max_profit = 0
    for i in prices:
        for j in prices[prices.index(i):]:
            if j-i >= max_profit:
                max_profit = j-i
    return max_profit

print(maxProfit([2,4,1]))  # 2
print(maxProfit([7,1,5,3,6,4]))  # 5
print(maxProfit([7,6,4,3,1]))  # 0
print('----------------')

# max_profit = price - min_price
def maxProfit2(prices: list) -> int:
    max_profit = 0
    min_price = prices[0]
    for i in prices:
        min_price = min(min_price, i) # find min price
        max_profit = max(max_profit, i - min_price) # max_profit = if i - min_price >= max_profit
    return max_profit

print(maxProfit2([2,4,1]))  # 2
print(maxProfit2([7,1,5,3,6,4]))  # 5
print(maxProfit2([7,6,4,3,1]))  # 0