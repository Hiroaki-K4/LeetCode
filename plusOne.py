from typing import Counter, List


class Solution:
	def plusOne(self, digits: List[int]) -> List[int]:
		digit = 0
		for i in digits:
			digit = digit * 10 + i
		digit += 1
		ans_list = []
		digit_str = str(digit)
		for i in digit_str:
			ans_list.append(int(i))
		return ans_list



if __name__ == '__main__':
	test = Solution()
	digits = [1,2,3]
	print(test.plusOne(digits))
	digits = [4,3,2,1]
	print(test.plusOne(digits))
	digits = [0]
	print(test.plusOne(digits))
	digits = [9]
	print(test.plusOne(digits))
	digits = [6,1,4,5,3,9,0,1,9,5,1,8,6,7,0,5,5,4,3]
	print(test.plusOne(digits))
