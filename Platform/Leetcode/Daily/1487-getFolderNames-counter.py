# encoding: utf-8
# author: Alan-learner

from Platform.Leetcode.Libs import *


class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        dic = defaultdict(int)  # 存储每个文件名的最小可行后缀
        ans = []
        for name in names:
            if name in dic:
                suf = dic[name]
                while f"{name}({suf})" in dic:
                    suf += 1
                ans.append(f"{name}({suf})")
                dic[name] = suf + 1
                dic[f"{name}({suf})"] = 1
            else:
                dic[name] = 1
                ans.append(name)
        return ans


def main():
    s = Solution()
    res = s.getFolderNames(["wano", "wano", "wano", "wano"])
    print(res)


if __name__ == '__main__':
    main()
