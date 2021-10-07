from typing import List


class Solution:
	def isAnagram(self, s: str, t: str) -> bool:
		s_dict = {}
		for word in s:
			if word in s_dict:
				s_dict[word] += 1
			else:
				s_dict[word] = 0
		s_dict = sorted(s_dict.items())
		t_dict = {}
		for word in t:
			if word in t_dict:
				t_dict[word] += 1
			else:
				t_dict[word] = 0
		t_dict = sorted(t_dict.items())
		if s_dict != t_dict:
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