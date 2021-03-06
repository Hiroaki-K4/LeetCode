from typing import List


# Definition for singly-linked list.
# class ListNode:
# 	def __init__(self, x):
# 		self.val = x
# 		self.next = None

class Solution:
	def deleteNode(self, node):
		"""
		:type node: ListNode
		:rtype: void Do not return anything, modify node in-place instead.
		"""
		node.val, node.next = node.next.val, node.next.next

if __name__ == '__main__':
	test = Solution()
	head = [4,5,1,9]
	node = 5
	test = Solution(node)
	