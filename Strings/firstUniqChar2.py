from typing import List


class Solution:
	def firstUniqChar(self, s: str) -> int:
		tmp_dict = {}
		for i in range(len(s)):
			if s[i] in tmp_dict:
				tmp_dict[s[i]] = -1
			else:
				tmp_dict[s[i]] = i
		for key in tmp_dict:
			if tmp_dict[key] != -1:
				return tmp_dict[key]
		return -1


if __name__ == '__main__':
	test = Solution()
	s = "leetcode"
	print(test.firstUniqChar(s))
	s = "loveleetcode"
	print(test.firstUniqChar(s))
	s = "aabb"
	print(test.firstUniqChar(s))