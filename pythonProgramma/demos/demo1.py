import requests
response = requests.get('https://httpbin.org/ip')
print('你的 IP 地址是 {0}'.format(response.json()['origin']))