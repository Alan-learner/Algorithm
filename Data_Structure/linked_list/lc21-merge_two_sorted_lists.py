# encoding: utf-8
# author: Alan-learner

from Platform.Leetcode.Libs import *


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # 空节点特判
        if not list1: return list2
        if not list2: return list1
        if list1.val > list2.val:
            # 一般性得将最小元素所在链表指定为list1
            list1, list2 = list2, list1
        pos = list1  # 始终指向待插入的位置
        pos1, pos2 = list1.next, list2  # 分别代表即将插入的两个节点的位置
        while pos1 or pos2:
            if not pos1:
                # 任意一个链表走到头了则合并完毕
                pos.next = pos2
                break
            if not pos2:
                pos.next = pos1
                break
            if pos1.val < pos2.val:
                # 选择合并较小的元素
                pos.next = pos1
                pos1 = pos1.next
            else:
                pos.next = pos2
                pos2 = pos2.next
            pos = pos.next
        return list1


def main():
    s = Solution()
    res = s
    print(res)


if __name__ == '__main__':
    main()
