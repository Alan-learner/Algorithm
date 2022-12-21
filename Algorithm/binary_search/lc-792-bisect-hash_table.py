# encoding: utf-8
# author: Alan-learner


from Leetcode.Libs import *


class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        # 返回words中，可作为s的子序列字符串的个数
        dic = defaultdict(list)
        for i, v in enumerate(s):
            # 下标i只增不减，天然有序，即便分散到不同hash表中也是有序的
            dic[v].append(i)
        ans = 0
        for word in words:
            idx = 0
            for i, c in enumerate(word):
                # 依次向后二分查找
                inx = bisect_left(dic[c], idx)
                if inx >= len(dic[c]):
                    break
                idx = dic[c][inx]
                idx += 1
            else:
                # 遍历完成，没有中途退出则符合条件
                ans += 1

        return ans


def main():
    s = Solution()
    res = s.numMatchingSubseq(s="abcde", words=["a", "bb", "acd", "ace"])
    print(res)


if __name__ == '__main__':
    main()
