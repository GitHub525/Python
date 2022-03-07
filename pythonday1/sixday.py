#coding:utf-8
import numpy
import datetime
#lambda表达式 lambda arguments:expression
x = lambda z:z+10
print x(5)
print "\r\n"
#lambda可以采用任意数量的参数
x = lambda a,b:a*b
print x(3,6)

#数组 要使用数组必须导入NumPy库函数
cars = ["Ford", "Volvo", "BMW"]
x = cars[0]
print x
print  "\r\n"

class MyClass:
  x = 5
p1 = MyClass()
print(p1.x)

#所有类都有一个名为 __init__() 的函数，该函数总是在类启动时执行。
#使用 __init__() 函数将值分配给对象属性或创建对象时必须执行的其他操作：
class Person:
  def __init__(self,name="aa",age=34):
    self.name = name
    self.age = age

# p1 = Person("John",36)
p1 = Person()
print p1.name
print p1.age
#迭代器
mytuple = ("apple","banana","cherry")
myit = iter(mytuple)
print next(myit)
print next(myit)
print next(myit)

x = dir(numpy)
print x

print "\r\n"
x = datetime.datetime.now()
print x
print x.year
print x.strftime("%A")
 