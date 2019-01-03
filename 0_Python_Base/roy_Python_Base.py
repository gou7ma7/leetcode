def func03():
    for value03 in range(1, 101):
        print(value03)


class Cls04(object):
    def __init__(self):
        self.value04s = range(1, 101)

    def print_value04(self):
        for self.value04 in self.value04s:
            print(self.value04)


if __name__ == "__main__":
    for value01 in range(1, 101):
        print(value01)
    # 第一种方法

    value02s = list(range(1, 101))
    # print(value02s)
    for value02 in value02s:
        print(value02)
    # 第二种方法

    func03()
    # 第三个方法

    value04 = Cls04()
    value04.print_value04()
    # 第四个方法
