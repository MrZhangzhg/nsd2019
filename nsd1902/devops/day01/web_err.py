from urllib import request, error

try:
    html = request.urlopen('http://127.0.0.1/abc')
except error.HTTPError as e:
    print('错误:', e)

try:
    html = request.urlopen('http://127.0.0.1/ban')
except error.HTTPError as e:
    print('错误:', e)
