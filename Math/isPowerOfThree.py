
class Solution:
	def isPowerOfThree(self, n: int) -> bool:
		if n == 0:
			return False
		while n % 3 == 0:
			n = int(n / 3)
		if n == 1:
			return True
		return False

if __name__ == '__main__':
	test = Solution()
	n = 27
	print(test.isPowerOfThree(n))
	n = 0
	print(test.isPowerOfThree(n))
	n = 9
	print(test.isPowerOfThree(n))
	n = 45
	print(test.isPowerOfThree(n))