from typing import List


class Solution:
	def firstUniqChar(self, s: str) -> int:
		tmp_dict = {}
		for char in s:
			if char in tmp_dict:
				tmp_dict[char] += 1
			else:
				tmp_dict[char] = 0
		for i in range(len(s)):
			if tmp_dict[s[i]] == 0:
				return i
		return -1


if __name__ == '__main__':
	test = Solution()
	s = "leetcode"
	print(test.firstUniqChar(s))
	s = "loveleetcode"
	print(test.firstUniqChar(s))
	s = "aabb"
	print(test.firstUniqChar(s))