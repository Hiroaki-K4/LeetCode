from typing import List


class Solution:
	def moveZeroes(self, nums: List[int]) -> None:
		zero_count = 0
		pos = 0
		for i in nums:
			if i != 0:
				nums[pos] = i
				pos += 1
			else:
				zero_count += 1
		while zero_count > 0:
			nums[-zero_count] = 0
			zero_count -= 1
		return nums


if __name__ == '__main__':
	test = Solution()
	nums = [0,1,0,3,12]
	print(test.moveZeroes(nums))
	nums = [0]
	print(test.moveZeroes(nums))
