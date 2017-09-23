from gevent import monkey; monkey.patch_socket()
import gevent

def f(n):
    for i in range(n):
	print gevent.getcurrent(), i
	gevent.sleep(0)

gr1 = gevent.spawn(f, 1000)
gr2 = gevent.spawn(f, 1000)
gr3 = gevent.spawn(f, 1000)

gr1.join()
gr2.join()
gr3.join()

#result output:
#<Greenlet at 0x7f618261ba50: f(5)> 0
#<Greenlet at 0x7f6182607050: f(5)> 0
#<Greenlet at 0x7f61826070f0: f(5)> 0
#<Greenlet at 0x7f618261ba50: f(5)> 1
#<Greenlet at 0x7f6182607050: f(5)> 1
#<Greenlet at 0x7f61826070f0: f(5)> 1
#<Greenlet at 0x7f618261ba50: f(5)> 2
#<Greenlet at 0x7f6182607050: f(5)> 2
#<Greenlet at 0x7f61826070f0: f(5)> 2
#<Greenlet at 0x7f618261ba50: f(5)> 3
#<Greenlet at 0x7f6182607050: f(5)> 3
#<Greenlet at 0x7f61826070f0: f(5)> 3
#<Greenlet at 0x7f618261ba50: f(5)> 4
#<Greenlet at 0x7f6182607050: f(5)> 4
#<Greenlet at 0x7f61826070f0: f(5)> 4
