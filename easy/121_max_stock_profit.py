"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.



Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.


Constraints:

1 <= prices.length <= 105
0 <= prices[i] <= 104
"""
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profits = [0]
        for index in range(len(prices)):
            profits.append(self.findProfit(prices[index+1::], prices[index]))
        # for
        return max(profits)
    # def

    def findProfit(self, prices: List[int], cur_price: int) -> int:
        # profit_price = list(filter(lambda x: x > cur_price, prices))
        profit_price = [x for x in prices if x > cur_price]
        max_price = max(profit_price) if len(profit_price) > 0 else cur_price
        return max_price - cur_price
    # def

    def maxProfitV2(self, prices: List[int]) -> int:
        profit = buy = 0
        for i in range(len(prices)):
            if prices[buy] > prices[i]:
                buy = i
            # if
            profit = max(profit, prices[i] - prices[buy])
        return profit
    # def
# class


solution = Solution()
print(solution.maxProfit([7, 1, 5, 3, 6, 4]))
print(solution.maxProfit([7, 6, 4, 3, 1]))
print(solution.maxProfit([2, 4, 1]))
print("==================")
print(solution.maxProfitV2([7, 1, 5, 3, 6, 4]))
print(solution.maxProfitV2([7, 6, 4, 3, 1]))
print(solution.maxProfitV2([2, 4, 1]))
