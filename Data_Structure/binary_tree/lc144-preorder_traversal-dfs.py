# encoding: utf-8
# author: Alan-learner

from Platform.Leetcode.Libs import *


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []

        def dfs(nd):
            if not nd:
                return
            nonlocal ans
            ans.append(nd.val)
            dfs(nd.left)
            dfs(nd.right)

        dfs(root)
        return ans


def main():
    s = Solution()
    res = s
    print(res)


if __name__ == '__main__':
    main()
