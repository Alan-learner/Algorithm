# encoding: utf-8
# author: Alan-learner

from Platform.Leetcode.Libs import *

isinstance()
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        # def dfs(nd):
        #     if not nd:
        #         return
        #     nonlocal ans
        #     dfs(nd.left)
        #     ans.append(nd.val)
        #     dfs(nd.right)
        # dfs(root)
        # return ans
        q = [(root,1)]
        while q:
            nd, col = q.pop()
            if not nd : continue
            if col == 1:
                q.append((nd.right,1))
                q.append((nd,0))
                q.append((nd.left,1))
            else:
                ans.append(nd.val)
        return ans


def main():
    s = Solution()
    res = s
    print(res)


if __name__ == '__main__':
    main()
