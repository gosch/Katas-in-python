import requests
response = requests.get('http://canyousolve.it/wl.svg')

with open('wl.svg', 'wb') as f:
    f.write(response.content)
