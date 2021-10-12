from typing import List


class Solution:
	def myAtoi(self, s: str) -> int:
		word_list = []
		ans_list = []
		for word in s:
			if not word.isspace():
				word_list.append(word)
		flag = 1
		if len(word_list) == 0:
			return 0
		if word_list[0] == '-' or word_list[0] == '+':
			if word_list[0] == '-':
				flag = -1
			word_list.pop(0)
		if len(word_list) == 0:
			return 0
		if not word_list[0].isdigit():
			return 0
		for word in word_list:
			if not word.isdigit():
				break
			ans_list.append(word)
		ans = int("".join(ans_list))
		ans = ans * flag
		if ans > 2147483647:
			ans = 2147483647
		if ans < -2147483648:
			ans = -2147483648
		return ans


if __name__ == '__main__':
	test = Solution()
	s = "42"
	print(test.myAtoi(s))
	s = "   -42"
	print(test.myAtoi(s))
	s = "4193 with words"
	print(test.myAtoi(s))
	s = "words and 987"
	print(test.myAtoi(s))
	s = "-91283472332"
	print(test.myAtoi(s))
	s = ""
	print(test.myAtoi(s))
	s = "+1"
	print(test.myAtoi(s))
	s = "   +0 123"
	print(test.myAtoi(s))
	s = "0032"
	print(test.myAtoi(s))