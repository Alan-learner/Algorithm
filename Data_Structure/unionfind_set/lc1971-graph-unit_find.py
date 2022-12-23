# encoding: utf-8
# author: Alan-learner

from Leetcode.Libs import *


class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        # 判断起始位置到目标位置之间是否有可行的路线，是否连通
        ufs = UnionFindSet(n)
        for edge in edges:
            x, y = edge
            # 统统加入并查集并合并
            ufs.merge(x, y)
        return ufs.find(source) == ufs.find(destination) # 看看二者代表元是否相同（是否连通）


def main():
    s = Solution()
    res = s
    print(res)


if __name__ == '__main__':
    main()
