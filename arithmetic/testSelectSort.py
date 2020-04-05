# 选择排序算法： 将乱序的list数列依次从小到大排列.
"""
算法逻辑：
1.内循环从左到右比较，小的置换到第0位，后面位数依次和第0位比较，如第n位<第0位则n位置换到第0位，
这样外循环第一次将最小的数字计算出排列到第0位；
2. 外循环第二次，在内循环中第1位到最后一位比较...外循环依次再循环最后一位的比较按升序排列完毕
"""


class TestSelectSort:
    def __init__(self):
        self.data = [4, 3, 5, 2, 1, 6, 7]
        self.except_data = [1, 2, 3, 4, 5, 6, 7]

    def produce(self):
        size = len(self.data)
        for i in range(size):
            min_data = i
            for j in range(i+1, size):
                if self.data[min_data] > self.data[j]:
                    min_data = j
                    print("此时的mindata", min_data)
                    self.data[i], self.data[j] = self.data[j], self.data[i]
                    print(self.data)
        return self.data


if __name__ == '__main__':
    test = TestSelectSort()
    test.produce()




