from typing import List


class Solution:
	def removeDuplicates(self, nums: List[int]) -> int:
		if len(nums) < 2:
			return len(nums)
		left = 0
		right = 1
		while right != len(nums):
			if nums[left] != nums[right]:
				nums[left + 1] = nums[right]
				left += 1
			right += 1
		return left + 1


if __name__ == '__main__':
	nums = [0,0,1,1,1,2,2,3,3,4]
	test = Solution()
	ans = test.removeDuplicates(nums)
	print(ans)