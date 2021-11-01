from typing import List

class Solution:
	def maxSubArray(self, nums: List[int]) -> int:
		ans = tmp_max = nums[0]
		for n in nums[1:]:
			tmp_max = max(n, tmp_max+n)
			ans = max(ans, tmp_max)
		return ans


if __name__ == '__main__':
	test = Solution()
	nums = [-2,1,-3,4,-1,2,1,-5,4]
	print(test.maxSubArray(nums))
	test = Solution()
	nums = [1]
	print(test.maxSubArray(nums))
	test = Solution()
	nums = [5,4,-1,7,8]
	print(test.maxSubArray(nums))