from urllib import request, error

url1 = 'http://127.0.0.1/abc'
url2 = 'http://127.0.0.1/ban'

try:
    request.urlopen(url1)
except error.HTTPError as e:
    print('错误:', e)

try:
    request.urlopen(url2)
except error.HTTPError as e:
    print('错误', e)
