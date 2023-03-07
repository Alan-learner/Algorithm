# encoding: utf-8
# author: Alan-learner

from Platform.Leetcode.Libs import *


class Solution:
    def longestDupSubstring(self, s: str) -> str:
        n = len(s)
        left = -1
        right = n

        # length 间隔越小，越有可能找到重复子串，具有二分性质
        def check(length: int) -> bool:
            st = set()
            for i in range(n - length + 1):
                sub = s[i:i + length]
                if sub in st:
                    # 找到了重复子串，说明长度可以增大
                    return True
                st.add(sub)
            return False

        while left + 1 < right:
            mid = (left + right) // 2
            if check(mid):
                left = mid
            else:
                right = mid
        st = set()
        for j in range(n - left + 1):
            sub = s[j:j + left]
            if sub in st:
                return sub
            st.add(sub)
        return ""


def main():
    s = Solution()
    res = s.longestDupSubstring(s="banana")
    print(res)


if __name__ == '__main__':
    main()
