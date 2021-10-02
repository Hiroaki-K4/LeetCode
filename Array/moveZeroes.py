from typing import List


class Solution:
	def moveZeroes(self, nums: List[int]) -> None:
		count = 0
		index = 0
		for i in nums:
			if i == 0:
				count += 1
			else:
				nums[index] = i
				index += 1
		while index < len(nums):
			nums[index] = 0
			index += 1
		return nums


if __name__ == '__main__':
	test = Solution()
	nums = [0,1,0,3,12]
	print(test.moveZeroes(nums))
	nums = [0]
	print(test.moveZeroes(nums))
