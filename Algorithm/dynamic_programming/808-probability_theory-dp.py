# encoding: utf-8
# author: Alan-learner


class Solution:
    def soupServings(self, n: int) -> float:
        # 将n份汤，按4种概率事件多阶段随机决策，求A、B汤被分完的概率
        n = (n + 24) // 25  # 将数据同比例放小，并向上取整，减小数据规模
        if n >= 179:
            # 根据解题要求精度剪枝，n越大，概率越接近1
            return 1.0
        # 定义 f(i,j) 为剩下i份A汤、j份B汤时的概率
        f = [[0.0] * (n + 1) for _ in range(n + 1)]
        f[0] = [0.5] + [1.0] * n
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                # 全概率公式, p * sum(子事件发生概率)
                f[i][j] = 0.25 * (f[max(i - 4, 0)][j] + f[max(i - 3, 0)][max(j - 1, 0)]
                                  + f[max(i - 2, 0)][max(j - 2, 0)] + f[i - 1][max(j - 3, 0)])
        return f[n][n]


def main():
    s = Solution()
    res = s
    print(res)


if __name__ == '__main__':
    main()
