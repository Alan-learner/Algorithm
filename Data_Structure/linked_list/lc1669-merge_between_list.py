# encoding: utf-8
# author: Alan-learner

from Platform.Leetcode.Libs import *


class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        # 将list1中a~b之间的节点替换为list2
        pos1 = list1
        pos2 = list2
        b = b - a + 2
        while a > 1:
            # 循环a次，找到第一个插入点
            a -= 1
            pos1 = pos1.next
        pos3 = pos1
        while b:
            # 找到第二个插入点
            b -= 1
            pos3 = pos3.next

        pos1.next = list2
        while pos2 and pos2.next:
            # 访问完list2，指针指向最后一个节点
            pos2 = pos2.next
        pos2.next = pos3
        return list1


def main():
    s = Solution()
    res = s
    print(res)


if __name__ == '__main__':
    main()
