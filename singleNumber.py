from typing import List


class Solution:
	# def singleNumber(self, nums: List[int]) -> int:
	# 	tmp_dict = {}
	# 	for i in nums:
	# 		if i in tmp_dict:
	# 			tmp_dict[i] += 1
	# 		else:
	# 			tmp_dict[i] = 1
	# 	for i in nums:
	# 		if tmp_dict[i] == 1:
	# 			return i
	def singleNumber(self, nums: List[int]) -> int:
		x = 0
		for n in nums:
			x = x ^ n
		return x



if __name__ == '__main__':
	test = Solution()
	nums = [2,2,1]
	print(test.singleNumber(nums))
	nums = [4,1,2,1,2]
	print(test.singleNumber(nums))
	nums = [1]
	print(test.singleNumber(nums))
