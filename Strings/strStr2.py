from typing import List


class Solution:
	def strStr(self, haystack: str, needle: str) -> int:
		if needle == "":
			return 0
		elif len(needle) > len(haystack):
			return -1
		for i in range(len(haystack)):
			if i + len(needle) > len(haystack):
				return -1
			elif haystack[i:i+len(needle)] == needle:
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
