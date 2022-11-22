[toc]
## 双指针
- - -
### 算法思想
- 对于连续数据（子数组、子串）求解符合条件的区间问题，通过枚举所有满足要求的左、右边界组，求解出答案
- - -
### 适用条件
1. 转移快速
    - 左右边界移动所需要的操作复杂度低
2. 单向性
    - 对于处理过后的元素无需再考虑；换言之，被边界越过的元素对后续答案没有影响
- - -
### 代码模板
```python
def get_ans(nums:list,target:int)->int:
    ans = float("inf")
    left = s = 0
    for right, v in enumerate(nums):
        s += v
        while s >= target: # 题目所要求的条件
            ans = min(ans, right - left + 1)
            s -= nums[left]
            left += 1
    return ans
```
- - -
### 示例

- [lc-3-最长无重复子串](same_direction/lc-3.py)

- [lc-209-和大于等于k最短子数组](same_direction/lc-209.py)

- [lc-713-乘积小于k的子数组个数](same_direction/lc-713.py)