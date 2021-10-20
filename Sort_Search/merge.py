from typing import List


class Solution:
	def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
		for i in range(m, m + n):
			nums1[i] = nums2[i - m]
		nums1.sort()
		return nums1

if __name__ == '__main__':
	test = Solution()
	nums1 = [1,2,3,0,0,0]
	m = 3
	nums2 = [2,5,6]
	n = 3
	print(test.merge(nums1, m, nums2, n))
	nums1 = [1]
	m = 1
	nums2 = []
	n = 0
	print(test.merge(nums1, m, nums2, n))
	nums1 = [0]
	m = 0
	nums2 = [1]
	n = 1
	print(test.merge(nums1, m, nums2, n))
	nums1 = [1,2,4,5,6,0]
	m = 5
	nums2 = [3]
	n = 1
	print(test.merge(nums1, m, nums2, n))