import requests
import gevent
import gevent.monkey
gevent.monkey.patch_all()

url = 'http://httpbin.org/ip'

def get(i):
	print("{}: {}".format(i, requests.get(url).text))
	
tasks = [gevent.spawn(get, i) for i in range(50)]
gevent.joinall(tasks)
