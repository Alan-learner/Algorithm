# encoding: utf-8
# author: Alan-learner

from Platform.Leetcode.Libs import *


class FreqStack:

    def __init__(self):
        self.data = defaultdict(list) # 根据频率动态存储不同的栈
        self.counter = Counter()
        self.heap = []  # 动态记录数据频率的最大值

    def push(self, val: int) -> None:
        self.counter[val] += 1
        self.data[self.counter[val]].append(val)
        heappush(self.heap, -self.counter[val])

    def pop(self) -> int:
        freq = - heappop(self.heap)
        val = self.data[freq].pop()
        self.counter[val] -= 1
        if self.counter[val] == 0:
            del self.counter[val]
        return val


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()


def main():
    s = Solution()
    res = s
    print(res)


if __name__ == '__main__':
    main()
