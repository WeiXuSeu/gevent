from gevent import monkey
monkey.patch_all()

import urllib2
from gevent import poll

def download(url):
	return urllib2.urlopen(url).read()
	
if __name__ == '__main__':
	urls = ['http://httpbin.org/get'] * 100
	pool = poll(20)
	print poll.map(download, urls)
