# encoding: utf-8
# author: Alan-learner

from Platform.Leetcode.Libs import *


class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        n = len(words)
        cnt = dict(zip(ascii_lowercase, score))
        @cache
        def dfs(idx: int, res: dict) -> int:
            if idx < 0:
                return 0

            result = dfs(idx - 1, res)  # 不选择当前物品
            cur = Counter(words[idx])
            if all(v <= res.get(k, 0) for k, v in cur.items()):
                # 满足可以选择的条件
                cur_score = sum(cnt[x] for x in words[idx])
                result = max(cur_score + dfs(idx - 1,
                                             res - cur), result)
            return result

        ct = Counter(letters)
        return dfs(len(words) - 1, ct)

        # back——tracing
        # def check(x: dict, y: dict) -> bool:
        #     for k, v in x.items():
        #         if k not in y or v > y[k]:
        #             return False
        #     return True
        #
        # def get_res(z: dict):
        #     res = 0
        #     for k, cnt in z.items():
        #         res += dic[k] * cnt
        #     return res
        #
        # for i, v in enumerate(score):
        #     dic[chr(ord("a") + i)] = v
        # cnt = Counter(letters)
        # for i in range(1, n+1):
        #     for c in combinations(words, i):
        #         f = lambda x, y: x + y
        #         s = reduce(f, list(c))
        #         # s = reduce(function=,sequence=)
        #         tmp = Counter(s)
        #         if check(tmp, cnt):
        #             ans = max(get_res(tmp), ans)
        # return ans


def main():
    s = Solution()
    res = s.maxScoreWords(words=["dog", "cat", "dad", "good"],
                          letters=["a", "a", "c", "d", "d", "d", "g", "o", "o"],
                          score=[1, 0, 9, 5, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    print(res)


if __name__ == '__main__':
    main()
