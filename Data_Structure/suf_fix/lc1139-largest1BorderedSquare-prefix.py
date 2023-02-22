# encoding: utf-8
# author: Alan-learner

from Platform.Leetcode.Libs import *


class Solution:
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        row_length = len(grid)
        col_length = len(grid[0])
        mx = min(row_length, col_length)
        ans = 0
        rol_prefix_list = [list(accumulate(lst)) for lst in grid]
        col_prefix_list = [list(accumulate(lst)) for lst in zip(*grid)]
        for start_row_idx in range(row_length):
            for start_col_idx in range(col_length):
                if grid[start_row_idx][start_col_idx] != 1:
                    continue
                tmp = ans
                for length in range(tmp, mx + 1):
                    end_row_idx = start_row_idx + length
                    end_col_idx = start_col_idx + length
                    if end_row_idx >= row_length:
                        break
                    if end_col_idx >= col_length:
                        break
                    if rol_prefix_list[start_row_idx][end_col_idx] - rol_prefix_list[start_row_idx][
                        start_col_idx] == length:
                        if rol_prefix_list[end_row_idx][end_col_idx] - rol_prefix_list[end_row_idx][
                            start_col_idx] == length:
                            if col_prefix_list[end_col_idx][end_row_idx] - col_prefix_list[end_col_idx][
                                start_row_idx] == length:
                                if col_prefix_list[start_col_idx][end_row_idx] - col_prefix_list[start_col_idx][
                                    start_row_idx] == length:
                                    ans = max(ans, length + 1)
        return ans ** 2


def main():
    s = Solution()
    # res = s.largest1BorderedSquare(grid=[[1, 1, 1], [1, 0, 1], [1, 1, 1]])
    # res = s.largest1BorderedSquare(grid=[[1, 1, 0, 0]])
    # res = s.largest1BorderedSquare(grid=[[0, 0, 0, 1]])
    res = s.largest1BorderedSquare(grid=[[1, 1], [1, 0]])
    print(res)


if __name__ == '__main__':
    main()
