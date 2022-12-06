# encoding: utf-8
# author: Alan-learner

from Leetcode.Libs import *


class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        # 词语压缩，根据长字符串压缩规则，返回可被压缩的word数量,模拟规则
        def get_pattern(x):
            pattern = []
            pre = s[0]
            step = 0
            for c in x:
                if c == pre:
                    step += 1
                else:
                    pattern.append((pre, step))
                    step = 1
                pre = c
            else:
                pattern.append((pre, step))
            return pattern

        ans = 0
        target = get_pattern(s)
        for word in words:
            tmp = get_pattern(word)
            if len(tmp) != len(target):
                continue
            for cur, tgt in zip(tmp, target):
                cur_c, cur_t = cur
                tgt_c, tgt_t = tgt
                if cur_c != tgt_c:
                    break
                if tgt_t < 3:
                    if tgt_t != cur_t:
                        break
                else:
                    if cur_t > tgt_t:
                        break
            else:
                ans += 1
        return ans


def main():
    s = Solution()
    res = s.expressiveWords(s="heeellooo", words=["hello", "hi", "helo"])
    print(res)


if __name__ == '__main__':
    main()
