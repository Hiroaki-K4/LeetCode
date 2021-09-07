from typing import List


class Solution:
	def maxProfit(self, prices: List[int]) -> int:
		ans = 0
		for i in range(len(prices)):
			if i == len(prices) - 1:
				continue
			ans += max(prices[i + 1] - prices[i], 0)
		return ans


if __name__ == '__main__':
	prices1 = [7,1,5,3,6,4]
	prices2 = [1,2,3,4,5]
	prices3 = [7,6,4,3,1]
	test = Solution()
	ans1 = test.maxProfit(prices1)
	print(ans1)
	ans2 = test.maxProfit(prices2)
	print(ans2)
	ans3 = test.maxProfit(prices3)
	print(ans3)
