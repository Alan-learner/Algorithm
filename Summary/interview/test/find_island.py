# encoding: utf-8
# author: Alan-learner

from Platform.Leetcode.Libs import *

"""
给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。

岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。

此外，你可以假设该网格的四条边均被水包围。

 

示例 1：

输入：grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
输出：1
示例 2：

输入：grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
输出：3

"""


class Solution:

    def find(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        result = 0

        def dfs(x, y):
            nonlocal grid
            grid[x][y] = 0
            for x_, y_ in (x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1):
                if 0 <= x_ < m and 0 <= y_ < n:
                    if grid[x_][y_] == "1":
                        dfs(x_, y_)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    result += 1
                    dfs(i, j)
        return result


def main():
    s = Solution()
    res = s.find(grid=[
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ])
    print(res)


if __name__ == '__main__':
    main()
