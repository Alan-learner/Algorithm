# encoding: utf-8
# author: Alan-learner

from typing import List


def divide(arr: List[int]) -> tuple:
    s = sum(arr)
    if s % 3 != 0:
        return [], [], []
    ans = []
    tmp = 0
    sub_arr = []
    for idx, val in enumerate(arr):
        tmp += val
        sub_arr.append(val)
        if tmp == s // 3:
            ans.append(sub_arr)
            tmp = 0
            sub_arr = []
            if len(ans) == 2 and idx < len(arr):
                ans.append(arr[idx + 1:])
                break

    ans = tuple(ans)
    if len(ans) < 3:
        return [], [], []
    return ans


def main():
    # res = divide(arr=[1, 2, 1, 2, 1, 2])
    res = divide(arr=[1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1])
    res = divide(arr=[1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1] * 2)
    print(res)


if __name__ == '__main__':
    main()
