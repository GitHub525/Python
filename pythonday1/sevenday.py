#coding:utf-8
import json
import re
#如果你有一个 JSON 字符串，你可以使用 json.loads()方法来解析它。
x =  '{ "name":"John", "age":30, "city":"New York"}'
y = json.loads(x)
print(y["age"])
print y
#如果您有一个 Python 对象，您可以使用该json.dumps()方法将其转换为 JSON 字符串。
x = {"name":"json",
     "age":"30",
     "city":"NewYork"}
y = json.dumps(x)
print y
print "\r\n"
txt = "The rain is Spain"
x = re.search("^The.*Spain$",txt)
print x.group()