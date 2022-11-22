# encoding: utf-8
# author: Alan-learner


from Leetcode.Libs import *


class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        dic = defaultdict(list)
        for i, v in enumerate(s):
            dic[v].append(i)
        ans = 0
        for word in words:
            idx = 0
            for i, c in enumerate(word):
                inx = bisect_left(dic[c], idx)
                if inx >= len(dic[c]):
                    break
                idx = dic[c][inx]
                idx += 1
            else:
                ans += 1

        return ans


def main():
    s = Solution()
    res = s.numMatchingSubseq(s="abcde", words=["a", "bb", "acd", "ace"])
    print(res)


if __name__ == '__main__':
    main()
