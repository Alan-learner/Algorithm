# encoding: utf-8
# author: Alan-learner

from Platform.Leetcode.Libs import *


# https://leetcode.cn/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 最长无重复子串
        cnt = Counter()
        ans = 0
        left = 0
        for right, c in enumerate(s):
            cnt[c] += 1
            while cnt[c] > 1:
                cnt[s[left]] -= 1
                left += 1
            if right - left + 1 > ans:
                ans = right - left + 1
        return ans


def main():
    s = Solution()
    res = s
    print(res)


if __name__ == '__main__':
    main()
