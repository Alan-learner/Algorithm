# encoding: utf-8
# author: Alan-learner

from Platform.Leetcode.Libs import *


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # ans = []
        # def dfs(nd):
        #     if not nd:
        #         return
        #     nonlocal ans
        #     dfs(nd.left)
        #     dfs(nd.right)
        #     ans.append(nd.val)

        # dfs(root)
        # return ans
        ans = []
        q = [root]
        while q:
            nd = q.pop()
            if nd is None:
                continue
            if isinstance(nd, TreeNode):
                q.append(nd.val)
                q.append(nd.right)
                q.append(nd.left)
            else:
                ans.append(nd)
        return ans


def main():
    s = Solution()
    res = s
    print(res)


if __name__ == '__main__':
    main()
