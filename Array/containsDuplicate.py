from typing import List

class Solution:
	def containsDuplicate(self, nums: List[int]) -> bool:
		tmp_dic = {}
		for i in nums:
			if i in tmp_dic:
				return True
			tmp_dic[i] = 0
		return False

if __name__ == '__main__':
	test = Solution()
	nums = [1,2,3,1]
	print(test.containsDuplicate(nums))
	nums = [1,2,3,4]
	print(test.containsDuplicate(nums))
	nums = [1,1,1,3,3,4,3,2,4,2]
	print(test.containsDuplicate(nums))
