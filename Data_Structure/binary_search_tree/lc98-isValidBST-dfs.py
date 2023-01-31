# encoding: utf-8
# author: Alan-learner

from Platform.Leetcode.Libs import *


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        ans = True

        def dfs(nd, left, right):
            nonlocal ans
            if not nd: return
            if nd.left:
                if nd.left.val >= nd.val or nd.left.val <= left:
                    ans = False
                    return
                dfs(nd.left, left, nd.val)
            if nd.right:
                if nd.right.val <= nd.val or nd.right.val >= right:
                    ans = False
                    return
                dfs(nd.right, nd.val, right)

        dfs(root, -inf, inf)
        return ans


def main():
    s = Solution()
    res = s
    print(res)


if __name__ == '__main__':
    main()
