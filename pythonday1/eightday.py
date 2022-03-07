#coding:utf-8

username = raw_input("Enter your name:"+"\r\n")
print "Username is :" +username

#字符串格式化
price = 40
txt = "The price is {} dollers"
print txt.format(price)
#利用索引
quantity = 3
itemno = 567
price = 49
myorder = "I want {0} pieces of item number {1} for {2:.2f} dollars."
print(myorder.format(quantity, itemno, price))
#命名索引
myorder = "I have a {carname}, it is a {model}."
print(myorder.format(carname = "Ford", model = "Mustang"))

