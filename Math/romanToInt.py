

class Solution:
	def romanToInt(self, s: str) -> int:
		ans = 0
		i = 0
		while i < len(s):
			if s[i] == 'I':
				if i + 1 < len(s):
					if s[i + 1] == 'V':
						ans += 3
						i += 1
					elif s[i + 1] == 'X':
						ans += 8
						i += 1
					ans += 1
				else:
					ans += 1
			elif s[i] == 'V':
				ans += 5
			elif s[i] == 'X':
				if i + 1 < len(s):
					if s[i + 1] == 'L':
						ans += 30
						i += 1
					elif s[i + 1] == 'C':
						ans += 80
						i += 1
					ans += 10
				else:
					ans += 10
			elif s[i] == 'L':
				ans += 50
			elif s[i] == 'C':
				if i + 1 < len(s):
					if s[i + 1] == 'D':
						ans += 300
						i += 1
					elif s[i + 1] == 'M':
						ans += 800
						i += 1
					ans += 100
				else:
					ans += 100
			elif s[i] == 'D':
				ans += 500
			elif s[i] == 'M':
				ans += 1000
			i += 1
		return ans


if __name__ == '__main__':
	test = Solution()
	s = "III"
	print(test.romanToInt(s))
	s = "IV"
	print(test.romanToInt(s))
	s = "IX"
	print(test.romanToInt(s))
	s = "LVIII"
	print(test.romanToInt(s))
	s = "MCMXCIV"
	print(test.romanToInt(s))
	s = "DCXXI"
	print(test.romanToInt(s))