import requests

url = 'http://news.baidu.com/news'

data = {
    'mid': '87B45F41B78082EBF0C5231806D12D52: FG = 1',
    'cuid': '',
    'ln': '18',
    'wf': '0',
    'action': '1',
    'down': '1',
    'display_time': '0',
    'withtoppic': '1',
    'orientation': '1',
    'from': 'news_webapp',
    'pd': 'webapp',
    'os': 'iphone',
    'nids': '',
    'remote_device_type': '1',
    'os_type': '1',
    'screen_size_width': '1920',
    'screen_size_height': '1080',
}

params = {
    'tn': 'bdapibaiyue',
    't': 'newchosenlist'
}

res = requests.post(url, data=data,)

print(res.json())
