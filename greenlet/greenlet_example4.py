import greenlet

def test1(x, y):
    z = gr2.switch(x + y)
    print('test1', z)
    xx = gr2.switch()
    print('test1', xx)

def test2(u):
    print('test2', u)
    gr3.switch('from test2')
    gr1.switch('return', 'from', 'test2')

def test3(u):
    print('test3', u);
    gr1.switch('return', 'from', 'test3')

gr1 = greenlet.greenlet(test1)
gr2 = greenlet.greenlet(test2)
gr3 = greenlet.greenlet(test3)
print gr1.switch("from", "test1")

#output
#('test2', 'fromtest1')
#('test3', 'from test2')
#('test1', ('return', 'from', 'test3'))
#('test1', ('return', 'from', 'test2'))
#None
