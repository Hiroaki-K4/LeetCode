from typing import List


class Solution:
	def reverse(self, x: int) -> int:
		ans = 0
		flag = 1
		if x < 0:
			x = x * (-1)
			flag = -1
		while x > 0:
			ans = ans * 10 + x % 10
			x = int(x / 10)
		ans = ans * flag
		if ans > 2147483647 or ans < -2147483648:
			ans = 0
		return ans

if __name__ == '__main__':
	test = Solution()
	x = 123
	print(test.reverse(x))
	x = -123
	print(test.reverse(x))
	x = 120
	print(test.reverse(x))
	x = 0
	print(test.reverse(x))
	x = 1534236469
	print(test.reverse(x))