## Python编程试讲
## 问题描述
- 给你一个整数数组 nums ，请你找出一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

- 子数组 是数组中的一个连续部分

### 线性dp算法

- 时间复杂度：O(n)
- 空间复杂度：O(1)
```python
from typing import  List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
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
```

### 分治算法
- 时间复杂度：O(n*log(n))
- 空间复杂度：O(1)
```python
from typing import  List
class Solution:
        def maxSubArray(self, nums: List[int]) -> int:
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
```
### 动态规划
- 时间复杂度：O(n^2)
- 空间复杂度：O(1)
```python
from math import inf
from typing import  List
class Solution:
        def maxSubArray(self, nums: List[int]) -> int:
            n = len(nums)
            ans = -inf
            for i in range(n):
                s = 0
                for j in range(i, n):
                    s += nums[j]
                    ans = max(ans, s)
            return ans
```

### 暴力模拟
- 时间复杂度：O(n^3)
- 空间复杂度：O(1)
```python
from math import inf
from typing import  List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        ans = -inf
        for i in range(n):
            for j in range(i + 1, n + 1):
                s = sum(nums[i:j])
                ans = max(ans, s)
        return ans
```