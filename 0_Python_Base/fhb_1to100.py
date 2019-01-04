#直接写
n = 1
sum = 0
while(n < 101):

    sum += n

    print(n)

    n = n + 1   
print(sum)


#数组

list1 = list(range(101))
sum = 0
for i in list1:

    print(i)

    sum += i;
print(sum)

#列表

def sum(x):
    print(x)
    if x == 1:
        return 1
    else:
        return sum(x - 1) + x
print(sum(100))

#类

class s(object):
    def __init__(self, num):
        self.num = num

    def Print_1toNum(self):
        i = 1
        while i < self.num + 1:
            print(i)
            i += 1

    def Sum(self):
        i = 1
        sum = 0
        while i < self.num + 1:
            sum += i
            i = i + 1
        print(sum)    
a = s(100)
a.Print_1toNum()
a.Sum()

