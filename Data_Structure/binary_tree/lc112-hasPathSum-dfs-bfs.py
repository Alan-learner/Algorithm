# encoding: utf-8
# author: Alan-learner

from Platform.Leetcode.Libs import *


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # ans = False
        # if not root: return False
        #
        # def dfs(nd, val):
        #     nonlocal ans
        #     if not nd:
        #         return
        #     val += nd.val
        #     if val == targetSum:
        #         if not nd.left:
        #             if not nd.right:
        #                 ans = True
        #     dfs(nd.left, val)
        #     dfs(nd.right, val)
        #
        # dfs(root, 0)
        # return ans

        if not root: return False
        q = [(root, 0)]
        while q:
            nd, sm = q.pop()
            sm += nd.val
            if sm == targetSum:
                if not (nd.left or nd.right):
                    return True
            if nd.left: q.append((nd.left, sm))
            if nd.right: q.append((nd.right, sm))
        return False


def main():
    s = Solution()
    res = s
    print(res)


if __name__ == '__main__':
    main()
