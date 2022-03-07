import requests

# header = {"User-Agent":"useragent"}
# url = "http://localhost/GET.php"
# getDate = {"username":"123","password":"admin"}
# # res = requests.get(url=url,params="111=4",headers=header,timeout=6)
#
# try:
#     res = requests.get(url,params=getDate)
#     print res.url
#     print res.text
# except Exception as e:
#     print "timeout"
# print res.request.headers
# print res.url
#
# dataPost = {"username":"admin","password":"password"}
# res = requests.post(url=url,data=dataPost)
# print res.request.body
# print res.text
# url = "http://localhost/upfile.php"
# upFile = {"userUpFile":open("test.py","rb")}
# postData = {"userSubmit":"submit"}
# res = requests.post(url=url,files=upFile,data=postData)
# print res.text