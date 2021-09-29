from typing import List


class Solution:
	def rotate(self, matrix: List[List[int]]) -> None:
		tmp_list = [[0] * len(matrix[0]) for i in range(len(matrix[0]))]
		for i in range(len(matrix)):
			matrix[len(matrix) - i - 1]
			for j in range(len(matrix[len(matrix) - i - 1])):
				tmp_list[j][i] = matrix[len(matrix) - i - 1][j]
		for i in range(len(tmp_list[0])):
			for j in range(len(tmp_list[0])):
				matrix[i][j] = tmp_list[i][j]
		return matrix

if __name__ == '__main__':
	test = Solution()
	matrix = [[1,2,3],[4,5,6],[7,8,9]]
	print(test.rotate(matrix))
	matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
	print(test.rotate(matrix))
	matrix = [[1,2,3],[4,5,6],[7,8,9]]
	print(test.rotate(matrix))
