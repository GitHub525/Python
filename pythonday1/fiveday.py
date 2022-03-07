#coding:utf-8
#函数 利用def来定义
def myfunction():
    print "This is my first function"
myfunction()
#函数还可以传参
def myname(name):
    print "my name is:"+name
myname("汪峰")
'''
从函数的角度来看：

参数是函数定义中括号内列出的变量。

参数是在调用函数时发送给函数的值。
'''
def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil", "Refsnes")

#!!任意参数*args
def myallargs(*args):
    print "这是任意参数:"+args[0]
myallargs("任意参数1","任意参数2")
#任意关键字参数数量**
def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")
#默认参数
def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")
print "\r\n"
#将列表作为参数传递
def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)
#要让函数返回值，请使用return语句
def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))
#function 不能定义为空 如果为空请放入pass
def myfunction():
  pass
#递归
