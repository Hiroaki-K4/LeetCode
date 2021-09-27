from typing import List




class Solution:
	def isValidSudoku(self, board: List[List[str]]) -> bool:
		for row in board:
			print(row)
			row_dict = {}
			for i in row:
				if i in row_dict and i != '.':
					return False
				row_dict[i] = 0
		for i in range(9):
			col_dict = {}
			for j in range(9):
				if board[j][i] in col_dict and board[j][i] != '.':
					return False
				col_dict[board[j][i]] = 0
		return (self.check3_3(board, 0, 0))

	def check3_3(self, board, row_start, col_start):
		check_dict = {}
		for i in range(row_start, row_start + 3):
			for j in range(col_start, col_start + 3):
				if board[i][j] in check_dict and board[i][j] != '.':
					print(check_dict)
					print(board[i][j])
					return False
				check_dict[board[j][i]] = 0
		return True
		

if __name__ == '__main__':
	test = Solution()
	board = [["5","3",".",".","7",".",".",".","."]
	,["6",".",".","1","9","5",".",".","."]
	,[".","9","8",".",".",".",".","6","."]
	,["8",".",".",".","6",".",".",".","3"]
	,["4",".",".","8",".","3",".",".","1"]
	,["7",".",".",".","2",".",".",".","6"]
	,[".","6",".",".",".",".","2","8","."]
	,[".",".",".","4","1","9",".",".","5"]
	,[".",".",".",".","8",".",".","7","9"]]
	print(test.isValidSudoku(board))