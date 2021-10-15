from typing import List


class Solution:
	def longestCommonPrefix(self, strs: List[str]) -> str:
		prefix = strs[0]
		for word in strs[1:]:
			while word[:len(prefix)] != prefix and prefix:
				prefix = prefix[:len(prefix) - 1]
			if not prefix:
				return prefix
		return prefix


if __name__ == '__main__':
	test = Solution()
	strs = ["flower","flow","flight"]
	print(test.longestCommonPrefix(strs))
	strs = ["dog","racecar","car"]
	print(test.longestCommonPrefix(strs))