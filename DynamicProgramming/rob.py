from typing import List

from typing import List


class Solution:
	def rob(self, nums: List[int]) -> int:
		dp = [0] * (len(nums) + 1)
		for i in range((len(nums))):
			dp[i + 1] = max(dp[i], dp[i - 1] + nums[i])
		return dp[-1]


if __name__ == '__main__':
	test = Solution()
	nums = [1,2,3,1]
	print(test.rob(nums))
	nums = [2,7,9,3,1]
	print(test.rob(nums))
	nums = [48,2,3,35]
	print(test.rob(nums))