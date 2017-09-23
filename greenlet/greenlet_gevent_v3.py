from gevent import monkey; monkey.patch_socket()
import gevent
import urllib2

def f(url):
    print("GET: %s" % url)
    response = urllib2.urlopen(url)
    data = response.read()
    print("%s bytes received from %s" % (len(data), url))

gevent.joinall([
    gevent.spawn(f, 'https://www.python.org'),
    gevent.spawn(f, 'https://www.yahoo.com'),
    gevent.spawn(f, 'https://github.com'),
])


#result output:
