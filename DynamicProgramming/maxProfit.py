from typing import List


class Solution:
	def maxProfit(self, prices: List[int]) -> int:
		diff = 0
		min = float('inf')
		for price in prices:
			if price < min:
				min = price
			elif price - min > diff:
				diff = price - min
		return diff


if __name__ == '__main__':
	test = Solution()
	prices = [7,1,5,3,6,4]
	print(test.maxProfit(prices))
	prices = [7,6,4,3,1]
	print(test.maxProfit(prices))