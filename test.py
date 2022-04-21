import requests

res = requests.get('https://google.com/nothing')
try:
    res.raise_for_status()
except Exception as exc:
    print('There was a problem %s' % (exc))