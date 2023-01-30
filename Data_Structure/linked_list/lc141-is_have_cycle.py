# encoding: utf-8
# author: Alan-learner

from Platform.Leetcode.Libs import *


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # 哈希表记录访问过的节点，判断是否有重复
        s = set()
        pos = head
        while pos:
            if pos in s:
                return True
            s.add(pos)
            pos = pos.next
        return False


def main():
    s = Solution()
    res = s
    print(res)


if __name__ == '__main__':
    main()
