# encoding: utf-8
# author: Alan-learner

from Platform.Leetcode.Libs import *


class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        ans = None

        def dfs(nd):
            if not nd: return
            nonlocal ans
            if nd.val == val:
                ans = nd
            elif nd.val > val:
                dfs(nd.left)
            else:
                dfs(nd.right)

        dfs(root)
        return ans


def main():
    s = Solution()
    res = s
    print(res)


if __name__ == '__main__':
    main()
