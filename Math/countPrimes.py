from typing import List
import math


class Solution:
	def countPrimes(self, n: int) -> int:
		if n <= 2:
			return 0
		nmap = [True for num in range(n)]
		res = 0
		i = 2
		while i*i < n:
			if nmap[i] == True:
				j = i*i
				while j < n:
					nmap[j] = False
					j += i
			i += 1
		for i in range(2, n):
			if nmap[i]:
				res += 1
		return res


if __name__ == '__main__':
	test = Solution()
	n = 10
	print(test.countPrimes(n))
	n = 0
	print(test.countPrimes(n))
	n = 1
	print(test.countPrimes(n))