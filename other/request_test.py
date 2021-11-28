import requests

r = requests.get('https://api.github.com/user', auth=('user', 'pass'))
print(r.headers['content-type'])
print(r.encoding)
print(r.status_code)
print(r.text)
print(r.json())
r.close()
# r = requests.post('https://httpbin.org/post', data={'key': 'value'})
# print(r.status_code)
# print(r.text)
