from typing import List
import itertools
import random


class Solution:
	def __init__(self, nums):
		self.array = nums
		self.original = list(nums)

	def reset(self):
		self.array = self.original
		self.original = list(self.original)
		return self.array

	def shuffle(self):
		aux = list(self.array)
		for idx in range(len(self.array)):
			remove_idx = random.randrange(len(aux))
			self.array[idx] = aux.pop(remove_idx)
		return self.array


if __name__ == '__main__':
	nums = [1, 2, 3]
	test = Solution(nums)
	print(test.reset())
	print(test.shuffle())
	nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
	test = Solution(nums)
	print(test.reset())
	print(test.shuffle())