from typing import List


class Solution:
	def strStr(self, haystack: str, needle: str) -> int:
		nl = len(needle)
		ml = len(haystack)
		if nl == 0:
			return nl
		if ml < nl:
			return -1
		for i in range(ml - nl + 1):
			if haystack[i:i+nl] == needle:
				return i
		return -1


if __name__ == '__main__':
	test = Solution()
	haystack = "hello"
	needle = "ll"
	print(test.strStr(haystack, needle))
	haystack = "aaaaa"
	needle = "bba"
	print(test.strStr(haystack, needle))
	haystack = ""
	needle = ""
	print(test.strStr(haystack, needle))
