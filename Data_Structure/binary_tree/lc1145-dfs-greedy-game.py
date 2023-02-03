# encoding: utf-8
# author: Alan-learner

from Platform.Leetcode.Libs import *


class Solution:
    def btreeGameWinningMove(self, root: Optional[TreeNode], n: int, x: int) -> bool:
        lsz = rsz = 0
        def dfs(nd):
            if not nd: return 0
            ls = dfs(nd.left)
            rs = dfs(nd.right)
            if nd.val == x:
                nonlocal lsz, rsz
                lsz,rsz = ls, rs
            return ls + rs + 1
        dfs(root)
        return max(lsz,rsz,n-lsz-rsz-1) * 2 > n

        return y > n - y


def main():
    s = Solution()
    res = s
    print(res)


if __name__ == '__main__':
    main()
