from typing import List


class Solution:
	def twoSum(self, nums: List[int], target: int) -> List[int]:
		for i in range(len(nums)):
			j = i + 1
			while j < len(nums):
				if nums[i] + nums[j] == target:
					return [i, j]
				j += 1

# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         memo = {}
#         for i in range(len(nums)):
#             needed = target - nums[i]
#             if needed in memo:
#                 return [memo[needed], i]
#             memo[nums[i]] = i

if __name__ == '__main__':
	test = Solution()
	nums = [2,7,11,15]
	target = 9
	print(test.twoSum(nums, target))
	nums = [3,2,4]
	target = 6
	print(test.twoSum(nums, target))
	nums = [3,3]
	target = 6
	print(test.twoSum(nums, target))
