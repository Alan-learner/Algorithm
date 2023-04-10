# encoding: utf-8
# author: Alan-learner

from Platform.Leetcode.Libs import *


class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        if not head:
            return []
        pos = head
        hp = []
        cnt = 0
        while pos:
            cnt += 1
            pos = pos.next
        pos2 = head
        ans = [0] * cnt
        loc = 0
        while pos2:
            while hp and pos2.val > hp[0][0]:
                val, idx = heappop(hp)
                ans[idx] = pos2.val
            heappush(hp, (pos2.val, loc))
            pos2 = pos2.next
            loc += 1
        return ans


def main():
    s = Solution()
    res = s
    print(res)


if __name__ == '__main__':
    main()
