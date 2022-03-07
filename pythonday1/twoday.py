#coding:utf-8
import random
#全局变量
x = "一辆车"
def myfunc():
    print "x全局拥有"+x
myfunc()
#局部变量
x = "一辆车"
def myfunc():
    x = "一艘船"
    print "x局部有"+x
myfunc()
print "x全局有"+x
#全局关键字，要在函数中创建全局变量可以用global
def myfunction():
    global x
    x = "global函数中创建全局变量"
myfunction()
print "函数内部"+x
#global 函数内部修改全局变量
x = "外部变量"
def function():
    global x
    x = "局部已修改全局变量"
function()
print "global修改成功"+x
a = '''文字类型：	str
数字类型：	int, float, complex
序列类型：	list, tuple, range
映射类型：	dict
套装类型：	set,frozenset
布尔类型：	bool
二进制类型：	bytes, bytearray, memoryview
'''
print a
print random.randrange(1,10)
b = "hello,World!"
print b
print len(b)
# print b[0]

for x in "banner":
    print x

txt = "The best things in life are free!"
print("free" in txt)

if "free" in  txt:
 print("Yes, 'free' is present.")

txt = "The best things in life are free!"
if "expensive" not in txt:
    print("No, 'expensive' is NOT present.")

b = "Hello World!"
print b[2:4]
print b[:5]
print(b[-5:-2])

a = "abcdefg"
print a.upper()
a = "ABCDEFG"
print a.lower()
#strip 删除开头和结尾的空格
a = "   a  b  c"
print a.strip()
#replance 替换字符串
print a.replace("a","x")
#split 拆分字符串
a = "Hello,World!"
print a.split(",")
#格式化字符串format
age = 30
text = "my age is {}"
print text.format(age)

quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))