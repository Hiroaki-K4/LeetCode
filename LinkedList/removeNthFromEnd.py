from typing import List
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
	def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
		return head


if __name__ == '__main__':
	test = Solution()
	head = [1,2,3,4,5]
	n = 2
	print(test.removeNthFromEnd(head, n))