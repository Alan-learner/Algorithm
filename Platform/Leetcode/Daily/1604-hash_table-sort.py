# encoding: utf-8
# author: Alan-learner

from Platform.Leetcode.Libs import *


class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        d = defaultdict(list)
        for name, t in zip(keyName, keyTime):
            t = int(t[:2]) * 60 + int(t[3:])  # 将每天的时间转化为绝对时间，便于排序比较
            d[name].append(t)
        ans = []
        for name, ts in d.items():
            if (n := len(ts)) > 2:
                ts.sort()
                for i in range(n - 2):
                    if ts[i + 2] - ts[i] <= 60:
                        ans.append(name)
                        break
        ans.sort()
        return ans


def main():
    s = Solution()
    res = s.alertNames(keyName=["daniel", "daniel", "daniel", "luis", "luis", "luis", "luis"],
                       keyTime=["10:00", "10:40", "11:00", "09:00", "11:00", "13:00", "15:00"])
    print(res)


if __name__ == '__main__':
    main()
