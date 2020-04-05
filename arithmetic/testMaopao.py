# 冒泡排序算法， 内循环依次升序两两对比将较小的调换到左边，外循环再循环n次直到遍历完所有的序列值


class TestMaoPao:
    def __init__(self):
        self.data = [1, 5, 3, 2, 4]
        self.except_data = [1, 2, 3, 4, 5]

    def produce(self, data: list):
        size = len(data)
        print(size)
        for i in range(size):
            print(i, 'i')
            for j in range(size - i - 1):
                print(j, 'j')
                if self.data[j] > self.data[j+1]:
                    self.data[j], self.data[j+1] = self.data[j+1], self.data[j]
                    print(self.data)
        return data

    def test_run(self):
        assert self.except_data == self.produce(self.data)


if __name__ == '__main__':
    T = TestMaoPao()
    T.test_run()
