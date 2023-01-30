# encoding: utf-8
# author: Alan-learner
import time
import random
from math import inf
from typing import List


# https://leetcode.cn/problems/maximum-subarray/

def timeit(func):
    def wrapper(*args, **kwargs):
        name = func
        for attr in ('__qualname__', '__name__'):
            if hasattr(func, attr):
                name = getattr(func, attr)
                break

        print("开始执行程序: {}".format(name))
        now = time.time()
        result = func(*args, **kwargs)
        using = (time.time() - now) * 1000
        msg = "执行时间: {:.1f}ms ,执行结果{}".format(using, result)
        print(msg)
        print("------------------------------")
        return result

    return wrapper


def generate_data(size: int) -> list:
    print("开始随机生成数据，数据规模为 {} ".format(size))
    print("------------------------------")
    lst = [random.randint(-100, 100) for _ in range(size)]
    print(lst)
    return lst


@timeit
def 线性dp(nums: List[int]) -> int:
    # 求最大（连续）子数组和
    ans = max_pre_sum = nums[0]
    # 动态规划，定义f[i]为以nums[i]结尾并且和最大的子（连续）数组
    for n in nums[1:]:
        # 考察当前元素对答案的贡献
        if max_pre_sum > 0:
            # 值为正，有贡献
            # f[i] += nums[i]
            max_pre_sum += n
        else:
            # 值为负，无贡献
            # f[i] = nums[i]
            max_pre_sum = n
        ans = max(ans, max_pre_sum)
    return ans


@timeit
def 递归分治(nums: List[int]) -> int:
    def divide(nums: list):
        length = len(nums)
        if length == 1:
            return nums[0], nums[0], nums[0], nums[0]
        mid = length // 2
        # 区间内以左边为端点的最大子段和、以右边边为端点的最大子段和
        # 最大子段和、区间和
        lsum1, rsum1, msum1, isum1 = divide(nums[:mid])
        lsum2, rsum2, msum2, isum2 = divide(nums[mid:])
        lsum = max(lsum1, isum1 + lsum2)
        rsum = max(rsum2, isum2 + rsum1)
        msum = max(rsum1 + lsum2, isum1 + isum2, msum1, msum2)
        isum = isum1 + isum2
        return lsum, rsum, msum, isum

    lsum, rsum, msum, isum = divide(nums)

    return msum


@timeit
def 动态规划(nums: List[int]) -> int:
    n = len(nums)
    ans = -inf
    for i in range(n):
        s = 0
        for j in range(i, n):
            s += nums[j]
            ans = max(ans, s)
    return ans


@timeit
def 暴力枚举(nums: List[int]) -> int:
    n = len(nums)
    ans = -inf
    for i in range(n):
        for j in range(i + 1, n + 1):
            s = sum(nums[i:j])
            ans = max(ans, s)
    return ans


def main():
    nums = generate_data(size=10)
    线性dp(nums)
    递归分治(nums)
    动态规划(nums)
    暴力枚举(nums)


if __name__ == '__main__':
    main()
