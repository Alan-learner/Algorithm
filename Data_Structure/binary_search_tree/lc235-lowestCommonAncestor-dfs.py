# encoding: utf-8
# author: Alan-learner

from Platform.Leetcode.Libs import *


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        father = defaultdict(TreeNode)
        father[root.val] = None

        def dfs(nd):
            nonlocal father
            if not nd: return
            if nd.left:
                father[nd.left.val] = nd
                dfs(nd.left)
            if nd.right:
                father[nd.right.val] = nd
                dfs(nd.right)

        dfs(root)
        x = p
        while x:
            y = q
            if x == y:
                return x
            while y:
                y = father[y.val]
                if x == y:
                    return x
            x = father[x.val]


def main():
    s = Solution()
    res = s
    print(res)


if __name__ == '__main__':
    main()
