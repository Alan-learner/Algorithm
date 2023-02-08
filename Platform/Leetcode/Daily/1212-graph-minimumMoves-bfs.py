# encoding: utf-8
# author: Alan-learner

from Platform.Leetcode.Libs import *


class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        # 有头有尾的贪吃蛇走迷宫，可平移、旋转
        n = len(grid)
        q = [(0, 0, 0, 1)]
        vis = set()
        step = 0
        while q:
            step += 1
            t = []
            for cur in q:
                x, y, a, b = cur
                nst_lst = [(x + 1, y, a, b),
                           (x, y + 1, a, b),
                           (x, y, a ^ 1, b ^ 1)]
                for nst in nst_lst:
                    if nst == (n - 1, n - 2, 0, 1):
                        return step
                    x_, y_, a_, b_ = nst
                    if nst not in vis:
                        if x_ + a_ < n and y_ + b_ < n:
                            if grid[x_ + a_][y_ + b_] == 0 and grid[x_][y_] == 0:
                                vis.add(nst)
                                t.append(nst)
            q = t
        return -1


def main():
    s = Solution()
    # res = s.minimumMoves(grid=[[0, 0, 0, 0, 0, 1],
    #                            [1, 1, 0, 0, 1, 0],
    #                            [0, 0, 0, 0, 1, 1],
    #                            [0, 0, 1, 0, 1, 0],
    #                            [0, 1, 1, 0, 0, 0],
    #                            [0, 1, 1, 0, 0, 0]])
    res = s.minimumMoves(grid=[[0, 0, 1, 1, 1, 1],
                               [0, 0, 0, 0, 1, 1],
                               [1, 1, 0, 0, 0, 1],
                               [1, 1, 1, 0, 0, 1],
                               [1, 1, 1, 0, 0, 1],
                               [1, 1, 1, 0, 0, 0]])
    print(res)


if __name__ == '__main__':
    main()
