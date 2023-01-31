# encoding: utf-8
# author: Alan-learner

from Platform.Leetcode.Libs import *


class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root: return TreeNode(val=val)

        def dfs(nd):
            if not nd:
                return
            elif nd.val > val:
                if not nd.left:
                    nd.left = TreeNode(val)
                    return
                dfs(nd.left)
            else:
                if not nd.right:
                    nd.right = TreeNode(val)
                    return
                dfs(nd.right)

        dfs(root)
        return root


def main():
    s = Solution()
    res = s
    print(res)


if __name__ == '__main__':
    main()
