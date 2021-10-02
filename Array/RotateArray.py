from typing import List


class Solution:
	def rotate(self, nums: List[int], k: int) -> None:
		"""
		Do not return anything, modify nums in-place instead.
		"""
		tmp_list = list(range(len(nums)))
		for i, digit in enumerate(nums):
			new_id = i + k
			while new_id >= len(nums):
				new_id = new_id - len(nums)
			tmp_list[new_id] = digit
		for i in range(len(tmp_list)):
			nums[i] = tmp_list[i]


if __name__ == '__main__':
	test = Solution()
	nums = [1,2,3,4,5,6,7]
	k = 3
	test.rotate(nums, k)
	nums = [-1,-100,3,99]
	k = 2
	test.rotate(nums, k)
	nums = [-1]
	k = 2
	test.rotate(nums, k)