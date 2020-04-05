# 测试弹栈压栈， 判断一个json数据结构是否是合法的
import time


class TestStack:
    def setup(self):
        self.data = []

    def push(self, input):
        self.data.append(input)

    def pop(self):
        return self.data.pop()

    def getSize(self):
        return len(self.data)

    def produce(self, item):
        for i in item:
            if i in "{{[":
                self.push(i)
            elif i in "]]}":
                self.pop()
            print("字符串%s" %i, self.data, self.getSize())
        # 返回0则表示是合法的json字符串
        return self.getSize()

    def testMatch(self):
        param = "{xx{uuu[uw]f}ewf}"
        assert self.produce(param) == True







