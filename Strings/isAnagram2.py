from typing import List


class Solution:
	def isAnagram(self, s: str, t: str) -> bool:
		if len(s) != len(t):
			return False
		s_dict = {}
		for s_word in s:
			if s_word in s_dict:
				s_dict[s_word] += 1
			else:
				s_dict[s_word] = 1
		for t_word in t:
			if t_word in s_dict:
				if s_dict[t_word] == 0:
					return False
				else:
					s_dict[t_word] -= 1
			else:
				return False
		return True


if __name__ == '__main__':
	test = Solution()
	s = "anagram"
	t = "nagaram"
	print(test.isAnagram(s, t))
	s = "rat"
	t = "car"
	print(test.isAnagram(s, t))