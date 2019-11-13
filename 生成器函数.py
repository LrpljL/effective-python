"""python 生成器"""
"""参考链接：https://blog.csdn.net/mieleizhi0522/article/details/82142856"""
"""生成器函数:yield vs return"""
"""生成器的__next__方法继续函数并且运行到下一个yield结果返回或引发一个stopiteration异常"""


def fun(n):
    for i in range(n):
        y = yield i
        print(y)


x = fun(5)
print(next(x))
x.send(2)
print(next(x))
"""
0
2
None
2
"""
# print(x.send(6))
# print(next(x))
# s = map((lambda x,y:x**2+y**2), [1,2,3],[4,5,6])
# for i in s:
#   print(i)
