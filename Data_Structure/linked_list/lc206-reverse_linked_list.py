# encoding: utf-8
# author: Alan-learner

from Platform.Leetcode.Libs import *
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # cur = head
        # pre = None
        # while cur:
        #     tmp = cur.next
        #     cur.next = pre
        #     pre = cur
        #     cur = tmp
        # return pre
        if head and head.next:
            new = self.reverseList(head.next)
            head.next.next = head
            head.next = None
            return new
        return head


def main():
    s = Solution()
    res = s
    print(res)


if __name__ == '__main__':
    main()
