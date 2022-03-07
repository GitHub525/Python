#coding:utf8
import json
#元组 tuple() 有序并且不可更改 允许重复
mytuple = ("apple","banana","cherry")
print mytuple
print len(mytuple)

onetuple = ("一项元组注意逗号",)
one = ("元组？不是")
print type(onetuple)
print type(one)
#!!将元组转化为列表
x = ("a","b","c")
y = list(x)
print y
print type(y)

#将元组添加到元组
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y
print(thistuple)
# set集合是无序、不可更改*和未索引的集合 不允许重复的
set = {"apple","banana","cherry"}
print set
set.add("other")
print set
#update 将一个集合添加到另一个集合中
#remove 如果目标不存在则会报错 discard 则不会引发错误
#pop 删除集合中最后一个项目
set.pop()
print set
#字典是有序*、可更改且不允许重复的集合。
thisdic = {"key1":"第一个键值"
           ,"key2":"第二个键值"
           ,"key3":"第三个键值"}
print json.dumps(thisdic,encoding='utf-8',ensure_ascii=False)
print thisdic["key1"]
x = thisdic.get("key2")
print x
z = thisdic.keys()
print z
y = thisdic.values()
print json.dumps(y,encoding="utf-8",ensure_ascii=False)
v = thisdic.items()
print json.dumps(v,encoding="utf-8",ensure_ascii=False)
if "第三个键值" in thisdic:
    print "值存在"
else:
    print "值不存在"
#update 更新字典
updatedic = {"1":"原始数据1",
             "2":"原始数据2",
             "3":"原始数据3"}
print json.dumps(updatedic,encoding="utf-8",ensure_ascii=False)
updatedic.update({"3":"原始数据已经更改"})
print json.dumps(updatedic,encoding="utf-8",ensure_ascii=False)
updatedic["4"] = "新添加的数据"
print json.dumps(updatedic,encoding="utf-8",ensure_ascii=False)
updatedic.update({"5":"利用新添加的数据5"})
print json.dumps(updatedic,encoding="utf-8",ensure_ascii=False)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
# thisdict.pop("model")
# print(thisdict)

for x in thisdict:
  print(x)
for x in thisdict:
    print thisdict[x]
print "\r\n"
for x in thisdict.values():
  print(x)

for x in thisdict.items():
    print json.dumps(x,y,encoding="utf-8",ensure_ascii=False)
#您不能简单地通过键入来复制字典dict2 = dict1，因为：dict2将只是对 的 引用，dict1并且在 中所做的更改 dict1也会自动在 中进行 dict2。
#有很多方法可以制作副本，一种方法是使用内置的 Dictionary 方法 copy()
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = dict(thisdict)
print(mydict)
''''
clear()	Removes all the elements from the dictionary
copy()	Returns a copy of the dictionary
fromkeys()	Returns a dictionary with the specified keys and value
get()	Returns the value of the specified key
items()	Returns a list containing a tuple for each key value pair
keys()	Returns a list containing the dictionary's keys
pop()	Removes the element with the specified key
popitem()	Removes the last inserted key-value pair
setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update()	Updates the dictionary with the specified key-value pairs
values()	Returns a list of all the values in the dictionary
'''
#while循环
i = 0
while i<10:
    print i
    i=i+1
#使用break可以推出循环 continue可以跳出循环进行下一次迭代
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)
print "\r\n"
#要循环一组代码指定的次数，我们可以使用range()函数，
#range()函数返回一个数字序列，默认从 0 开始，递增 1（默认），并以指定的数字结束。
for i in range(6):
    print i
print "\r\n"
for x in range(2, 6):
  print(x)

print "\r\n"
for x in range(2, 30, 3):
  print(x)
print "\r\n"
for x in range(6):
  print(x)
else:
  print("Finally finished!")