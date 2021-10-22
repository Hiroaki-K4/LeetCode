

class Solution:
	def __init__(self, bad):
		self.bad_version = bad

	def isBadVersion(self, version):
		if version >= self.bad_version:
			return True
		return False

	# def firstBadVersion(self, n):
	# 	for i in range(n):
	# 		if self.isBadVersion(i + 1):
	# 			return i + 1
	# 	return n

	def firstBadVersion(self, n):
		left = 1
		right = n
		while (left < right):
			mid = int(left + (right - left) / 2)
			if (self.isBadVersion(mid)):
				right = mid
			else:
				left = mid + 1
		return left


if __name__ == '__main__':
	n = 5
	bad = 4
	test = Solution(bad)
	print(test.firstBadVersion(n))
	n = 1
	bad = 1
	test = Solution(bad)
	print(test.firstBadVersion(n))
	n = 2126753390
	bad = 1702766719
	test = Solution(bad)
	print(test.firstBadVersion(n))