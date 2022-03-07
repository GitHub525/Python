#coding:utf-8
import os
'''在 Python 中处理文件的关键函数是 open()函数。
该open()函数有两个参数； 文件名和模式。
打开文件有四种不同的方法（模式）：
"r"- 读取 - 默认值。打开文件进行读取，如果文件不存在则出错
"a"- Append - 打开一个文件进行追加，如果文件不存在则创建该文件
"w"- 写入 - 打开文件进行写入，如果文件不存在则创建文件
"x"- 创建 - 创建指定文件，如果文件存在则返回错误
此外，您可以指定文件是否应作为二进制或文本模式处理
"t"- 文本 - 默认值。文本模式
"b"- 二进制 - 二进制模式（例如图像）
'''
#read(参数int) 指定返回的字符数 readline 表示读取一行
file = open("oneday.py","rt")
# print file.read()
print file.readline()
#for逐行循环读取
for x in file:
    print x
#读完文件调用close()函数关闭文件
file.close()
'''要写入现有文件，必须向 open()函数添加参数：
"a"- 追加 - 将追加到文件的末尾
"w"- 写入 - 将覆盖任何现有内容'''
# appendfile = open("oneday.py","a")
# appendfile.write("#这是追加的内容")
# appendfile.close()
'''要在 Python 中创建新文件，请使用open()带有以下参数之一的方法：
"x"- 创建 - 将创建一个文件，如果文件存在则返回错误
"a"- Append - 如果指定的文件不存在，将创建一个文件
"w"- 写入 - 如果指定的文件不存在，将创建一个文件'''
# newfile = open("tenday.py","a")
# newfile.close()
#要删除文件，您必须导入 OS 模块，并运行其 os.remove()功能：
# os.remove("tenday.py")
#
txt = "Hello World"[::-1]
print(txt)