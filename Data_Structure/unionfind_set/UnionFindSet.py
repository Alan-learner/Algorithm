# encoding: utf-8
# author: Alan-learner


class UnionFindSet:
    def __init__(self, length: int):
        self.father = list(range(length))
        self.size = [1] * length

    def find(self, x: int) -> int:
        if self.father[x] != x:
            # 路径压缩
            self.father[x] = self.find(self.father[x])
        return self.father[x]

    def merge(self, a: int, b: int):
        fa = self.find(a)
        fb = self.find(b)
        self.father[fa] = fb
        self.size[fb] += self.size[fa]


def main():
    pass


if __name__ == '__main__':
    main()
