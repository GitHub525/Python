#coding:utf-8

# print 9>2
# x = "Hello"
# y = 15
#
# print(bool(x))
# print(bool(y))
# print bool(False)
# print bool(None)
# print bool(0)
# print bool("")
# print bool(())
# print bool([])
# print bool({})
#列表 用于将多个项目存储在单个变量中用[]表示
#列表项是有序的、可更改的，并且允许重复值。
thislist = ["apple","banana","cherry"]
print thislist
print len(thislist)
print type(thislist)
'''
List是一个有序且可变的集合。允许重复成员。
元组是一个有序且不可更改的集合。允许重复成员。
Set是一个无序、不可更改*和无索引的集合。没有重复的成员。
字典是一个有序的集合**和可变的。没有重复的成员。
'''
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print len(thislist)
thislist[0] = "aaaaaaa"
# thislist.insert(1,"bbbbbbbbbbbb")
thislist.append("bbbbbbb")
print thislist
print len(thislist)


a = ['1','2','3']
b = ['4','5','6']
a.append(b)
print a

thislist = ["apple", "banana", "cherry"]
print thislist
thislist.pop()
print(thislist)

hislist = ["apple", "banana", "cherry"]
print len(hislist)
for i in range(len(hislist)):
  print(hislist[i])

print '\r\n'
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1
print '\r\n'

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)

# def myfunc(n):
#   return abs(n - 50)
#
# thislist = [100, 50, 65, 82, 23]
# thislist.sort(key = myfunc)
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# mylist = thislist.copy()
# print(mylist)

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)
