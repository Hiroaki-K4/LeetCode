from typing import List


class Solution:
	def reverseString(self, s: List[str]) -> None:
		for i in range(0, int(len(s) / 2)):
			tmp = s[i]
			s[i] = s[len(s) - i - 1]
			s[len(s) - i - 1] = tmp
		return s


if __name__ == '__main__':
	test = Solution()
	s = ["h","e","l","l","o"]
	print(test.reverseString(s))
	s = ["H","a","n","n","a","h"]
	print(test.reverseString(s))