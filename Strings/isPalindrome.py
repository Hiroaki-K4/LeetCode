from typing import List


class Solution:
	def isPalindrome(self, s: str) -> bool:
		word_list = []
		s = s.lower()
		for word in s:
			if (word.isalnum()):
				word_list.append(word)
		i = 0
		while i < len(word_list) / 2:
			if word_list[i] != word_list[len(word_list) - 1 - i]:
				return False
			i += 1
		return True


if __name__ == '__main__':
	test = Solution()
	s = "A man, a plan, a canal: Panama"
	print(test.isPalindrome(s))
	s = "race a car"
	print(test.isPalindrome(s))
	s = "0P"
	print(test.isPalindrome(s))